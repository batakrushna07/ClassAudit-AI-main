3.12

# 🎓 ClassAudit AI — Smart Face Recognition Attendance System

> **AI-powered face recognition attendance and class monitoring system built for modern educational institutions.**

ClassAudit AI is a full-stack Django web application that automates teacher attendance tracking and live class monitoring using real-time face recognition. It features a **role-based dual-portal system** — one for **Principals** (admins) and one for **Teachers** — each with dedicated dashboards, analytics, and management tools.

---

## ✨ Key Features

### 🔐 Authentication
- **Face Recognition Login** — Teachers can log in by scanning their face via webcam (powered by `face_recognition` + `OpenCV`)
- **Password Login** — Traditional username/password login available for both roles
- **Role-Based Access Control** — Separate portals, dashboards, and permissions for Principals and Teachers

### 👨‍💼 Principal Portal
- **Dashboard** — Overview of all teachers grouped by department, real-time present/absent statistics
- **Teacher Management** — Add, view, and delete teachers with face registration (captures 5 images for embedding)
- **Timetable Scheduling** — Create and manage weekly class schedules for each teacher
- **Teacher Reports** — Detailed attendance reports with date/month/year filtering
- **Performance Analysis** — Visual charts showing departmental distribution, top teachers, and active presence duration
- **Defaulter Export** — Export CSV reports of teachers who missed attendance, filtered by department, day, month, and year

### 👩‍🏫 Teacher Portal
- **Dashboard** — Welcome banner, today's scheduled classes, class history, and a calendar widget
- **Profile** — Personal information, monthly attendance statistics (present, late, absent), and class report history
- **Mark Attendance** — Face-based daily attendance check-in via webcam
- **Start Class** — Launch a scheduled class session from the timetable
- **Live Class Monitoring** — Real-time face verification during class sessions, tracking active presence duration with periodic checks every 5 seconds
- **Previous Records** — Filterable history of all past class sessions
- **Help Center** — FAQ section for platform guidance

### 🤖 Face Recognition Engine
- **Multi-Image Enrollment** — Captures 5 face images during teacher registration for robust embedding
- **128-Dimensional Face Embeddings** — Uses `dlib`'s deep learning model via `face_recognition` library
- **Averaged Embeddings** — Combines multiple captures for higher accuracy
- **Configurable Match Threshold** — Default `0.45` distance threshold for face comparison
- **Live Verification** — Continuous face checks during class monitoring to ensure teacher presence

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.12, Django 4.2 |
| **Database** | SQLite3 |
| **Face Recognition** | `face_recognition`, `dlib`, `OpenCV`, `NumPy` |
| **Frontend** | HTML5, CSS3 (modular per-page CSS), JavaScript (vanilla) |
| **Charts** | Chart.js |
| **Icons** | Font Awesome 6.4 |
| **Fonts** | Plus Jakarta Sans, Bungee, Nunito, Inter |

---

## 📁 Project Structure

```
face-recognition-authentication/
│
├── facere/                          # Django project config
│   ├── settings.py                  # Project settings (SQLite, timezone: Asia/Kolkata)
│   ├── urls.py                      # URL routing (27 routes)
│   ├── wsgi.py                      # WSGI entry point
│   └── asgi.py                      # ASGI entry point
│
├── accounts/                        # Main application
│   ├── models.py                    # Database models (6 models)
│   ├── views.py                     # All view logic (~1460 lines)
│   ├── admin.py                     # Django admin configuration
│   ├── utils/                       # Face recognition utilities
│   │   ├── face_detector.py         # Face detection (location finding)
│   │   ├── face_embedding.py        # Face encoding (128-dim vectors)
│   │   └── face_matcher.py          # Face comparison (distance threshold)
│   │
│   └── templates/                   # HTML templates (19 files)
│       ├── home.html                # Landing page with animated hero
│       ├── login.html               # Face recognition login
│       ├── teacher_login.html       # Teacher password login
│       ├── principal_login.html     # Principal password login
│       ├── principal_register.html  # Principal registration
│       ├── principal_dashboard.html # Principal main dashboard
│       ├── principal_analysis.html  # Performance analytics & charts
│       ├── teacher_analysis.html    # Individual teacher analysis
│       ├── add_teacher.html         # Add teacher with face capture
│       ├── schedule_teacher.html    # Manage teacher timetable
│       ├── teacher_reports.html     # Teacher attendance reports
│       ├── teacher_dashboard.html   # Teacher main dashboard
│       ├── teacher_profile.html     # Teacher profile & stats
│       ├── mark_attendance.html     # Face-based attendance check-in
│       ├── live_class_monitoring.html # Real-time class monitoring
│       ├── previous_records_teacher.html # Class session history
│       ├── teacher_help.html        # Help & FAQ page
│       ├── sidebar_principal.html   # Reusable principal sidebar
│       └── sidebar_teacher.html     # Reusable teacher sidebar
│
├── static/
│   ├── css/                         # Stylesheets (18 files)
│   │   ├── style.css                # Global/base styles
│   │   ├── admin_theme.css          # Principal portal theme
│   │   ├── teacher_theme.css        # Teacher portal theme
│   │   ├── home.css                 # Landing page styles
│   │   ├── login.css                # Face login page
│   │   ├── principal_login.css      # Principal login page
│   │   ├── principal_register.css   # Principal registration
│   │   ├── principal_dashboard.css  # Principal dashboard
│   │   ├── principal_analysis.css   # Analytics page
│   │   ├── teacher_analysis.css     # Teacher analysis page
│   │   ├── teacher_dashboard.css    # Teacher dashboard
│   │   ├── teacher_login.css        # Teacher login
│   │   ├── teacher_help.css         # Help page
│   │   ├── teacher_reports.css      # Reports page
│   │   ├── add_teacher.css          # Add teacher page
│   │   ├── mark_attendance.css      # Attendance page
│   │   ├── schedule_teacher.css     # Schedule page
│   │   └── live_class_monitoring.css # Live monitoring page
│   └── img/                         # Static images
│
├── user_faces/                      # Uploaded teacher face images
├── db.sqlite3                       # SQLite database
├── manage.py                        # Django management script
└── requirements.txt                 # Python dependencies
```

---

## 🗃️ Database Models

### `Principal`
| Field | Type | Description |
|---|---|---|
| `user` | OneToOne → User | Django auth user |
| `school_name` | CharField(100) | Name of the school/institution |

### `Teacher`
| Field | Type | Description |
|---|---|---|
| `user` | OneToOne → User | Django auth user |
| `principal` | ForeignKey → Principal | School the teacher belongs to |
| `name` | CharField(100) | Full name |
| `department` | CharField(10) | Department code (CS, MATH, PHY, etc.) |

### `Timetable`
| Field | Type | Description |
|---|---|---|
| `teacher` | ForeignKey → Teacher | Assigned teacher |
| `subject` | CharField(100) | Subject name |
| `day` | CharField(3) | Day of week (MON–SAT) |
| `start_time` | TimeField | Class start time |
| `end_time` | TimeField | Class end time |

### `TeacherAttendance`
| Field | Type | Description |
|---|---|---|
| `teacher` | ForeignKey → Teacher | Teacher who checked in |
| `date` | DateField (auto) | Date of attendance |
| `time` | TimeField (auto) | Check-in time |
| `status` | CharField(20) | Present / Late |

### `ClassSession`
| Field | Type | Description |
|---|---|---|
| `teacher` | ForeignKey → Teacher | Teacher conducting class |
| `timetable` | ForeignKey → Timetable | Linked timetable slot (nullable) |
| `start_time` | DateTimeField (auto) | Session start |
| `end_time` | DateTimeField | Session end |
| `total_active_duration` | DurationField | Verified active presence time |
| `status` | CharField(20) | Ongoing / Completed |
| `monitoring_resumption_count` | IntegerField | Number of face re-verifications |

### `UserImages`
| Field | Type | Description |
|---|---|---|
| `user` | ForeignKey → User | Associated user |
| `face_image` | ImageField | Stored face photo for recognition |

---

## 🛣️ URL Routes

| URL | View | Description |
|---|---|---|
| `/` | `home` | Landing page |
| `/principal/register/` | `principal_register` | Principal sign-up |
| `/principal/login/` | `principal_login_view` | Principal login |
| `/principal/dashboard/` | `principal_dashboard` | Principal dashboard |
| `/add-teacher/` | `add_teacher` | Add teacher with face registration |
| `/principal/delete-teacher/<id>/` | `delete_teacher` | Remove a teacher |
| `/principal/schedule/<id>/` | `schedule_teacher` | Manage teacher schedule |
| `/principal/reports/<id>/` | `view_teacher_reports` | Teacher attendance reports |
| `/principal/analysis/` | `principal_analysis` | Performance analytics |
| `/principal/teacher-analysis/<id>/` | `teacher_analysis` | Individual teacher analysis |
| `/principal/export-defaulters/` | `export_defaulter_csv` | Export defaulter CSV |
| `/principal/delete-schedule/<id>/` | `delete_schedule` | Delete a schedule entry |
| `/principal/delete-all-schedule/<id>/` | `delete_all_schedule` | Delete all schedules for teacher |
| `/login/` | `login_user` | Face recognition login |
| `/teacher/login-password/` | `teacher_login_password` | Teacher password login |
| `/teacher/dashboard/` | `teacher_dashboard` | Teacher dashboard |
| `/teacher/profile/` | `teacher_profile` | Teacher profile page |
| `/teacher/mark-attendance/` | `mark_attendance` | Face-based attendance |
| `/teacher/start-class/<id>/` | `start_class` | Start a class session |
| `/teacher/live-monitoring/` | `live_class_monitoring` | Live face monitoring |
| `/teacher/update-live-attendance/` | `update_live_attendance` | Periodic face check API |
| `/teacher/end-class/` | `end_class` | End class session |
| `/teacher/records/` | `previous_records_teacher` | Past class records |
| `/teacher/help/` | `teacher_help` | Help & FAQ |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **CMake** (required for `dlib` compilation)
- **pip** (Python package manager)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/face-recognition-authentication.git
cd face-recognition-authentication

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install django face_recognition opencv-python numpy Pillow

# 4. Apply database migrations
python3 manage.py migrate

# 5. Run the development server
python3 manage.py runserver 4000
```

### First-Time Setup

1. Open `http://127.0.0.1:4000/` in your browser
2. Click **"Register as Principal"** to create an admin account
3. Log in to the **Principal Dashboard**
4. Add teachers via **"Add Teacher"** (captures 5 face images via webcam)
5. Set up class timetables via **"Schedule"**
6. Teachers can now log in via **face recognition** or **password** and use their portal

---

## 🔄 How Face Recognition Works

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   Registration    │     │   Face Login      │     │  Live Monitoring  │
│                   │     │                   │     │                   │
│  Capture 5 imgs   │     │  Capture 1 frame  │     │  Every 5 seconds  │
│       ↓           │     │       ↓           │     │       ↓           │
│  face_recognition │     │  face_recognition │     │  face_recognition │
│  .face_encodings()│     │  .face_encodings()│     │  .face_encodings()│
│       ↓           │     │       ↓           │     │       ↓           │
│  Average 5 embeds │     │  Compare with DB  │     │  Compare with DB  │
│       ↓           │     │       ↓           │     │       ↓           │
│  Store in DB      │     │  distance < 0.45? │     │  Track duration   │
│                   │     │  → Login success  │     │  → Update session │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

---

## 📸 Pages Overview

| Page | Portal | Description |
|---|---|---|
| 🏠 **Home** | Public | Animated landing page with face scan hero animation |
| 🔑 **Face Login** | Public | Webcam-based facial recognition login |
| 📊 **Principal Dashboard** | Principal | Teacher overview, department stats, present/absent counts |
| 📈 **Analysis** | Principal | Charts for department distribution, top teachers, active hours |
| 👤 **Add Teacher** | Principal | Teacher registration with live face capture |
| 📅 **Schedule** | Principal | Weekly timetable management |
| 📋 **Reports** | Principal | Filterable attendance reports per teacher |
| 🏡 **Teacher Dashboard** | Teacher | Today's classes, history, calendar widget |
| 👤 **Profile** | Teacher | Monthly stats, attendance charts, class history |
| ✅ **Mark Attendance** | Teacher | Daily face-based check-in |
| 📹 **Live Monitoring** | Teacher | Real-time face tracking during class |
| 📖 **Records** | Teacher | Past class session history |
| ❓ **Help** | Teacher | FAQ and support |

---

## 🛠️ Configuration

Key settings in `facere/settings.py`:

| Setting | Value | Description |
|---|---|---|
| `TIME_ZONE` | `Asia/Kolkata` | Timezone for attendance timestamps |
| `DEBUG` | `True` | Development mode (set `False` for production) |
| `STATIC_URL` | `static/` | Static file serving path |
| `DATABASE` | `SQLite3` | Default database engine |

---

## 📄 License

This project is for educational purposes.

---

<p align="center">
  <b>Built with ❤️ using Django & Face Recognition</b>
</p>
