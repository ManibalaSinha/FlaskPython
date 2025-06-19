from flask import Flask, jsonify, request #give code access to third party libraries
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os

app = Flask(__name__) #set to Flask Constructor, will take name from script
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'C:\\Users\\manib\\FlaskPython\\students.db' 

db = SQLAlchemy(app)

@app.cli.command('db_create')
def db_create():
   db.create_all()
   print('Database created!')


@app.cli.command('db_drop')
def db_drop():
   db.drop_all()
   print('Database dropped!')


@app.cli.command('db_seed')
def db_seed():
   america = Student(student_name='America', student_class =5, student_subject ='python', student_interest ='Flask', student_grade=1.1, student_city= 'cty')
   africa = Student(student_name='Africa', student_class =7, student_subject ='plugin', student_interest ='api', student_grade=2.1, student_city= 'ity')
   australia = Student(student_name='Australia', student_class =9, student_subject ='django', student_interest ='rest', student_grade=1.3, student_city= 'cit')

   db.session.add(america) 
   db.session.add(africa)  
   db.session.add(australia) 

   test_user = User(first_name='Ram', last_name='Shayam', email='user@test.com', password='password')

   db.session.add(test_user)
   db.session.commit()
   print('Database seeded!')


@app.route('/')# @ decorator gives special capabilities to function , define route of end point
def hello_world():
   return 'Hello Kidz Learning Stations!'


@app.route('/shorts')
def shorts():
   return jsonify(message='Hello from the Kidz Learning Stations'), 200


@app.route('/not_found')
def not_found():
   return jsonify(message='That resource was not found'), 404


@app.route('/parameters')
def parameters():
   name = request.args.get('name') #give access to all url values
   age = int(request.args.get('age'))
   if age < 18:
      return jsonify(message="Sorry " + name + ", you are not old enough."), 401
   else:
      return jsonify(message="Welcome " + name + ", you are old enough")


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
   if age < 18:
      return jsonify(message="Sorry " + name + ", you are not old enough."), 401
   else:
      return jsonify(message="Welcome " + name + ", you are old enough!")
   
@app.route('/students', methods=['GET']) #respond to GET request, method we want to accept
def students(): # want to get all data from databse students
   students_list = Student.query.all()
   result = students_schema.dump(students_list)
   return jsonify(result.data)


#database models
class User(db.Model):
   __tablename__ = 'users'
   id = db.Column(Integer, primary_key=True)
   first_name = db.Column(String)
   last_name = db.Column(String)
   email = db.Column(String, unique=True)
   password = Column(String)


class Student(db.Model):
   __tablename__ = 'students'
   student_id = Column(Integer, primary_key=True)
   student_name = Column(String)
   student_class = Column(Integer)
   student_subject = Column(String)
   student_interest = Column(String)
   student_grade = Column(Float)
   student_city = Column(String)


if __name__ == '__main__':
   app.run()