from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow

# App setup
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'students.db')

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(Integer, primary_key=True)
    student_name = db.Column(String)
    student_class = db.Column(Integer)
    student_subject = db.Column(String)
    student_interest = db.Column(String)
    student_grade = db.Column(Float)
    student_city = db.Column(String)

class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# CLI Commands
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database created!")

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print("Database dropped!")

@app.cli.command('db_seed')
def db_seed():
    s1 = Student(student_name="America", student_class=5, student_subject="Python", student_interest="Flask", student_grade=1.1, student_city="NYC")
    s2 = Student(student_name="Africa", student_class=7, student_subject="Django", student_interest="API", student_grade=2.5, student_city="LA")
    db.session.add_all([s1, s2])
    db.session.commit()
    print("Database seeded!")

# Routes
@app.route('/')
def hello():
    return "Hello from Kidz Learning Stations!"

# --- CRUD ROUTES FOR STUDENT ---

# CREATE student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student(
        student_name=data.get('student_name'),
        student_class=data.get('student_class'),
        student_subject=data.get('student_subject'),
        student_interest=data.get('student_interest'),
        student_grade=data.get('student_grade'),
        student_city=data.get('student_city')
    )
    db.session.add(student)
    db.session.commit()
    return student_schema.jsonify(student), 201

# READ all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return students_schema.jsonify(students), 200

# READ single student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return student_schema.jsonify(student), 200

# UPDATE student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    data = request.get_json()

    student.student_name = data.get('student_name', student.student_name)
    student.student_class = data.get('student_class', student.student_class)
    student.student_subject = data.get('student_subject', student.student_subject)
    student.student_interest = data.get('student_interest', student.student_interest)
    student.student_grade = data.get('student_grade', student.student_grade)
    student.student_city = data.get('student_city', student.student_city)

    db.session.commit()
    return student_schema.jsonify(student), 200

# DELETE student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify(message="Student deleted successfully"), 200

# ------------------------

if __name__ == '__main__':
    app.run(debug=True)
