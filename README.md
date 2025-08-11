# Kidz Learning Stations - Flask API

A simple Flask REST API project demonstrating  CRUD operations and database management with SQLite, SQLAlchemy ORM, and Marshmallow serialization.
Python Flask CRUD App | Build Full Stack Web App with SQLite
https://youtu.be/6A-Et2R4lvM
---

## Features

* Flask backend API with SQLite database
* SQLAlchemy ORM models for `User` and `Student`
* Database management CLI commands:

  * `flask db_create` - create database tables
  * `flask db_drop` - drop all tables
  * `flask db_seed` - seed database with sample data
* API endpoints with URL parameters and query parameters
* JSON responses using Flask’s `jsonify`
* Input handling with Flask’s `request`

---

## Installation

1. Clone this repository

   ```bash
   git clone https://github.com/manibalasinha/PythonFlask.git
   cd PythonFlask
   ```

2. (Optional but recommended) Create a virtual environment and activate it

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Create the database tables

   ```bash
   flask db_create
   ```

2. Seed the database with sample data

   ```bash
   flask db_seed
   ```

3. Run the Flask app

   ```bash
   flask run
   ```

4. Open your browser or API client and test the endpoints:

   * `GET /` - Welcome message
   * `GET /shorts` - Simple JSON message
   * `GET /not_found` - 404 JSON response
   * `GET /parameters?name=John&age=20` - Parameterized response
   * `GET /url_variables/John/20` - URL path variables response
   * `GET /students` - Get all students in the database

---

## Project Structure

```
PythonFlask/
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── students.db          # SQLite database file (generated)
└── README.md            # This file
```

---

## Dependencies

* Flask
* Flask-SQLAlchemy
* SQLAlchemy
* Marshmallow
* Flask-Marshmallow

---

## Notes

* Database URI is set to a local SQLite file at `C:\Users\manib\FlaskPython\students.db`. Adjust path in `app.py` if needed.
* Use Flask CLI commands to manage your database easily.

---

## License

This project is licensed under the MIT License.
