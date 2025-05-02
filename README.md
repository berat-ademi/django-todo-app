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

---

## 📦 Setup Instructions

1. Clone the repository

   `git clone https://github.com/berat-ademi/django-todo-app.git`

   `cd django-todo-app`

2. Create a virtual environment

   `python -m venv venv`

   `source venv/bin/activate`

   (On Windows: `venv\Scripts\activate`)

3. Install dependencies

   `pip install -r requirements.txt`

4. Apply migrations

   `python manage.py migrate`

5. (Optional) Seed the database with one user and some tasks

   `python manage.py populate_db`

   ✅ Creates:
   - user: `testuser`
   - password: `password123`
   - email: `testuser@example.com`
   - profile with default image
   - tasks from `tasks/fixtures/tasks_fixture.json`

6. Run the development server

   `python manage.py runserver`

7. Open in your browser

   http://127.0.0.1:8000/

---

## 🧪 Testing

Run basic tests with:

   `python manage.py test`


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
├── manage.py
├── db.sqlite3
├── README.md
├── .gitignore
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
├── todolist/                     # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
```

---

## 🔒 Admin Login (optional)

To access the Django admin panel:

1. Create a superuser (if you haven't already):

   `python manage.py createsuperuser`

2. Follow the prompts to set `username`, `email`, and `password`.

3. Then visit the admin panel:

   http://127.0.0.1:8000/admin

Use your superuser credentials to log in.

---