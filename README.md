# Full Stack Data Engineer Demo Task

## Project Overview
This is a simple Django web application that demonstrates:

- Basic CRUD functionality via REST APIs.
- Integration with an external API (fetching random jokes).
- A simple data visualization/report page.

The application includes:

1. `/api/items/` – REST API endpoints for creating, reading, updating, and deleting items.
2. `/report/` – HTML page that displays a random joke fetched from a public API.

---

## Project Structure

Project Task/
├── api/ # Django app containing views, models, and APIs
├── core/ # Django project settings
├── templates/ # HTML templates
├── db.sqlite3 # SQLite database
├── manage.py
└── README.md

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/tejas7588/fullstack-data-engineer-demo_Task.git
cd fullstack-data-engineer-demo_Task
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt

pip install django djangorestframework requests

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

Access the application:

Open http://127.0.0.1:8000/report/
 to see the report page.

Open http://127.0.0.1:8000/api/items/
 to test CRUD operations.

# Initialize Git repo (if not already)
git init

# Add remote origin (only if not added)
git remote add origin https://github.com/tejas7588/fullstack-data-engineer-demo_Task.git

# Add all files
git add .

# Commit changes
git commit -m "Initial commit"

# Push to GitHub
git push -u origin main

git remote set-url origin https://github.com/tejas7588/fullstack-data-engineer-demo_Task.git

Notes

The random joke is fetched from the public API: https://official-joke-api.appspot.com/random_joke

SQLite is used for simplicity; PostgreSQL can be configured in settings.py for production.

This is a demo project, so DEBUG mode is enabled.


