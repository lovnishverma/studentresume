from flask import Flask, request, render_template, send_from_directory, g, redirect, url_for, flash
import os
import sqlite3
from datetime import datetime
import pytz
from dotenv import load_dotenv

load_dotenv()  # Load .env

app = Flask(__name__)
app.secret_key = 'nielitisgreat'  # Needed for flashing messages

UPLOAD_FOLDER = "uploads"
DATABASE = "files.db"
DELETE_PASSWORD = os.getenv("DELETE_PASSWORD")

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Database helper functions
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        db.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT UNIQUE NOT NULL,
                description TEXT,
                size INTEGER,
                uploaded_at TEXT
            )
        """)
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@app.route("/", methods=["GET", "POST"])
def upload_file():
    db = get_db()
    if request.method == "POST":
        file = request.files["file"]
        description = request.form.get("description", "").strip()

        if file:
            ist = pytz.timezone("Asia/Kolkata")
            current_datetime = datetime.now(ist).strftime("%d-%m-%Y %I:%M %p")

            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            file_size = os.path.getsize(file_path)

            try:
                db.execute(
                    "INSERT INTO files (filename, description, size, uploaded_at) VALUES (?, ?, ?, ?)",
                    (file.filename, description, file_size, current_datetime)
                )
                db.commit()
            except sqlite3.IntegrityError:
                flash("File already exists!", "danger")
                return redirect(url_for("upload_file"))

            flash("File uploaded successfully.", "success")
            return redirect(url_for("upload_file"))

    files = db.execute("SELECT * FROM files ORDER BY uploaded_at DESC").fetchall()
    total_files = len(files)
    ist = pytz.timezone("Asia/Kolkata")
    current_year = datetime.now(ist).strftime("%Y")

    return render_template("index.html", files=files, total_files=total_files, year=current_year)

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)

@app.route("/delete/<int:file_id>", methods=["POST"])
def delete_file(file_id):
    entered_password = request.form.get("password", "")
    if entered_password != DELETE_PASSWORD:
        flash("Incorrect password!", "danger")
        return redirect(url_for("upload_file"))

    db = get_db()
    file = db.execute("SELECT * FROM files WHERE id = ?", (file_id,)).fetchone()

    if file:
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file["filename"])
        if os.path.exists(file_path):
            os.remove(file_path)

        db.execute("DELETE FROM files WHERE id = ?", (file_id,))
        db.commit()
        flash("File deleted successfully.", "success")
    else:
        flash("File not found.", "warning")

    return redirect(url_for("upload_file"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
