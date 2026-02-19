Django Contact & CV Application

A simple Django application that includes:

Contact form system

Message storage

Admin panel management

CV upload & download system

Environment-based configuration

📌 What This Project Does
🔹 Contact System

Users can submit a contact form (name, email, subject, message)

Messages are saved to the database

Messages can be managed via Django admin panel

Email sending is supported (SMTP configuration required)

🔹 CV Download System

CV files are managed from the Django admin panel

Uploaded CV files appear in the navbar

Users can download the active CV directly from the website

⚠️ Important:
To make the CV download button visible and functional:

Go to Admin Panel

Open the Document section

Upload your CV file

Save it

After uploading, the CV will appear in the navbar and can be downloaded.

🛠 Technologies Used

Python

Django 6.0.2

SQLite (default database)

Pillow

🚀 How to Run This Project Locally
1️⃣ Clone the Repository
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

http://127.0.0.1:8000/

Admin panel:

http://127.0.0.1:8000/admin/
📧 Email Configuration (Required for Contact Form)

To enable email sending, configure SMTP settings in settings.py:

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "your-smtp-host"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your-email"
EMAIL_HOST_PASSWORD = "your-email-password"
DEFAULT_FROM_EMAIL = "your-email"

⚠️ If not configured, the contact form will save messages to the database but will not send emails.

🔐 Environment Variables (Optional for Production)

Example:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_HOST=your-smtp-host
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-password

If not configured, the project runs in development mode.

📂 Requirements
asgiref==3.11.1
Django==6.0.2
pillow==12.1.1
sqlparse==0.5.5
tzdata==2025.3

📝 Notes

Default database is SQLite
SECRET_KEY is not hardcoded
CV must be uploaded from admin panel to enable download
Virtual environment folder is not included in the repository