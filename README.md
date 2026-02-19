🚀 Django Contact & CV Application

A Django-based portfolio application that includes a contact form system and dynamic CV upload/download functionality via the admin panel.

📌 Features
📩 Contact System

Users can submit a contact form (name, email, subject, message)

Messages are stored in the database

Messages are manageable via Django Admin

Email sending supported (SMTP configuration required)

📄 CV Download System

CV files are uploaded via Django Admin

Uploaded CV automatically appears in the navbar

Users can download the active CV directly from the website

⚠️ To enable CV download:

Go to /admin/

Open Document

Upload your CV

Save

🛠 Technologies

Python

Django 6.0.2

SQLite (default)

Pillow

⚙️ Installation (Run Locally)
1️⃣ Clone Repository
git clone <your-repository-url>
cd <project-folder>
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Migrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run Server
python manage.py runserver

Open in browser:

Main site → http://127.0.0.1:8000/
Admin panel → http://127.0.0.1:8000/admin/

📧 Email Configuration (Required for Contact Form)

To enable email sending, configure SMTP settings in settings.py:

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "your-smtp-host"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your-email"
EMAIL_HOST_PASSWORD = "your-email-password"
DEFAULT_FROM_EMAIL = "your-email"

If not configured, messages will be saved to the database but emails will not be sent.

🔐 Environment Variables (Optional for Production)

Example configuration:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_HOST=your-smtp-host
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-password
📦 Requirements
asgiref==3.11.1
Django==6.0.2
pillow==12.1.1
sqlparse==0.5.5
tzdata==2025.3
📝 Notes

Default database: SQLite

SECRET_KEY is not hardcoded

CV must be uploaded from admin panel to activate download

venv/ is excluded from repository

👨‍💻 Author

Barış
