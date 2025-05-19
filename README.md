# 📝 ToDoApp – Code Challenge Submission

A simple, user-specific to-do list application built with Django. Authenticated users can create, edit, and manage personal tasks with notes and due dates.

---

## 🚀 Features

- User authentication (signup / login / logout)
- Personal task dashboard
- Create, update, complete, and delete tasks
- Task filtering by status (completed / pending)
- Due date and optional notes for each task
- Profile picture upload (bonus feature)
- Responsive UI using Bootstrap
- Dockerized setup for development and production environments
- Environment-based configuration using `.env` files

---

### Prerequisites

- Docker
- Docker Compose
- Alternatively: Python 3.9+ and pip (for manual setup)

---

## 📦 Setup Instructions

### ⚙️ Environment Configuration

1. Copy the example environment file:

```bash
cp .env.template .env
```

2. Edit `.env` and replace placeholder values with your local credentials and secret key.

---

### 🐳 Using Docker (Recommended)

1. Build and start the containers:

```bash
docker-compose up --build
```

2. Create a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

3. Access the app:

- Application: http://localhost:8000  
- Admin panel: http://localhost:8000/admin

---

### 💻 Manual Setup (Without Docker)

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. (Optional) Seed the database with one user and some tasks:

```bash
python manage.py populate_db
```

✅ Creates:
- user: `testuser`
- password: `password123`
- email: `testuser@example.com`
- profile with default image
- tasks from `tasks/fixtures/tasks_fixture.json`

5. Run the development server:

```bash
python manage.py runserver
```

6. Open in your browser:

http://127.0.0.1:8000/

---

## 🧪 Testing

Run basic tests with:

```bash
python manage.py test
```

---

## 🛠️ Tech Stack

- Django
- Bootstrap 5
- SQLite
- Python 3.11+

---

## 📁 Project Structure

```plaintext
django_todo_app/          # Root project folder
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── db.sqlite3
├── README.md
├── .gitignore
├── .env.template                 # Example env file for setup
├── media/                        # For uploaded/profile images
│   └── profile_pics/
│       └── default.jpg
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── registration/             # login.html, signup.html
│   └── tasks/                    # dashboard.html, task_form.html, confirm_delete.html
├── tasks/                        # Tasks app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── fixtures/
│   │   └── tasks_fixture.json
│   └── management/
│       └── commands/
│           └── populate_db.py
├── users/                        # Users app (auth + profiles)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
└── todolist/                     # Django project settings
    ├── settings.py
    ├── urls.py
    └── ...
```

---

## 🔒 Admin Login (optional)

To access the Django admin panel:

1. Create a superuser (if you haven't already):

```bash
python manage.py createsuperuser
```

2. Follow the prompts to set `username`, `email`, and `password`.

3. Visit the admin panel:

http://127.0.0.1:8000/admin

Use your superuser credentials to log in.

---
