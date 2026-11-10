# 💼 JobTrack - Job Application Tracker & Analytics Dashboard

A modern, responsive web application built with **Django** and **Bootstrap 5** designed to streamline, track, and visualize your job search journey. Monitor application statuses, interview schedules, monthly application trends, and personal notes—all in one centralized dashboard.

---

## 🚀 Key Features

- **🔐 User Authentication & Security**
  - Email-based sign-in and user registration.
  - Password strength validation and secure session management.
  - User isolation: every user only accesses their own job applications.

- **📊 Comprehensive Analytics Dashboard**
  - **KPI Summary Cards**: Immediate counts for Total Jobs, Applied, Interviews Scheduled, and Offers/Selected.
  - **Status Breakdown Chart**: Visual representation of applications across stages (*Interested*, *Applied*, *Interview*, *Selected*, *Rejected*) powered by Chart.js.
  - **Monthly Trend Chart**: Track your application volume over time to maintain consistency.

- **📝 Full Job Application Management (CRUD)**
  - Add, edit, update, and delete job postings with ease.
  - Detailed metadata tracking:
    - Company Name & Role Title
    - Job Location (City, Onsite, Hybrid, or Remote)
    - Salary / CTC offered
    - Direct Job Application Link
    - Application Date & Interview Date
    - Comprehensive Job Description & Personal Notes

- **🔍 Search & Filter Tools**
  - Real-time search across company names and job titles.
  - One-click status filter to isolate specific hiring stages.

- **🎨 Clean & Responsive UI**
  - Responsive design powered by Bootstrap 5.
  - Polished modern layout with subtle card elevations and custom styles.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Django 5.x
- **API Framework**: Django REST Framework
- **Database**: SQLite3 (default for local development; MySQL compatible via PyMySQL)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5.3
- **Data Visualization**: Chart.js

---

## 📂 Project Structure

```text
JobTrack/
│
├── config/                  # Django project root configuration
│   ├── asgi.py
│   ├── settings.py          # Project settings, apps & middleware
│   ├── urls.py              # Root routing configuration
│   └── wsgi.py
│
├── jobs/                    # Core JobTrack application
│   ├── migrations/          # Database schema migrations
│   ├── static/jobs/         # Custom stylesheets and scripts
│   │   ├── css/style.css
│   │   └── js/script.js
│   ├── templates/           # Application and auth templates
│   │   ├── jobs/
│   │   │   ├── base.html
│   │   │   ├── dashboard.html
│   │   │   └── job_form.html
│   │   └── registration/
│   │       ├── login.html
│   │       └── register.html
│   ├── admin.py             # Admin panel registration
│   ├── forms.py             # Application & authentication forms
│   ├── models.py            # JobApplication database schema
│   ├── urls.py              # Application route definitions
│   └── views.py             # Business logic & dashboard metrics
│
├── .gitignore               # Ignored files (venv, sqlite db, cache)
├── manage.py                # Django CLI utility
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Installation & Local Setup

Follow these steps to run the application locally:

### 1. Clone the Repository
```bash
git clone https://github.com/Triveni-Pyhon-Dev/JobTrack.git
cd JobTrack
```

### 2. Create and Activate a Virtual Environment

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## 📌 Usage Flow

1. **Register**: Create an account with your username and email address.
2. **Log In**: Sign in using your registered email and password.
3. **Add Job**: Click **Add New Job** to record details of a position you're tracking.
4. **Update Status**: Keep application statuses up-to-date as you hear back from recruiters.
5. **View Insights**: Review your progress and distribution charts directly from the dashboard.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

