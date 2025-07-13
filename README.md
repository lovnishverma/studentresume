# 📄 Resume Uploader - Flask App

A modern, clean, and secure **Resume Uploader** built with Flask, Bootstrap 5, and SQLite.
This app allows students to upload, manage, and delete their resumes securely via a password-protected admin panel.

---

## 🚀 Features

✅ Upload PDF resumes with student names

✅ View all uploaded resumes with size, name, and upload date

✅ Secure download option for resumes

✅ Admin-only secure delete with password from `.env`

✅ Fully responsive modern UI (Bootstrap 5 + FontAwesome + Google Fonts)

✅ Glassmorphism & Animated modern design

✅ Flash messages for user feedback

✅ Timezone: **Asia/Kolkata (IST)**

---

## 📂 Project Structure

```
├── app.py                # Main Flask Application
├── templates/
│   └── index.html        # Bootstrap + Modern Styled UI
├── uploads/              # Directory for storing uploaded files
├── files.db              # SQLite database for file metadata
├── requirements.txt      # Python dependencies
├── .env                  # Secret environment variables
└── README.md             # Documentation (this file)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/resume-uploader.git
cd resume-uploader
```

### 2️⃣ Create `.env` File

```
DELETE_PASSWORD=your_secure_delete_password
```

---

### 3️⃣ Install Dependencies

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### `requirements.txt`

```
Flask
pytz
python-dotenv
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

Navigate to:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🔑 Functionality Summary

### 🖥️ Upload Section

* Only `.pdf` allowed
* Files stored under `uploads/`
* Descriptions are typically student names.

### 📊 Dashboard

* View list of uploaded resumes with metadata.
* Shows: **File Name**, **Size (bytes)**, **Upload Date (IST)**.

### ⬇️ Download

* Files available via **Download** button.

### ❌ Secure Delete

* Password stored in `.env` checked on delete request.
* Deletes both database entry and file.

---

## 📌 Important Notes

* Duplicate file names are blocked.
* `.env` password keeps deletion secure.
* Upload limit per file: **10MB max (enforced client-side JS)**.

---

## 🖼️ Sample Screenshot


<img width="1777" height="967" alt="image" src="https://github.com/user-attachments/assets/76d819f0-c763-4100-99e3-f1b7e6867d32" />


---

## 👨‍💻 Author

**Lovnish Verma**
🔗 [https://lovnishverma.github.io/](https://lovnishverma.github.io/)

---

## 📃 License

For educational and demonstration purposes only.
No commercial use without permission.

---
