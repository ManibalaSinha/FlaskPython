from app import app, db
from flask import request, jsonify
from models import User
from schemas import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/users", methods=["POST"])
def add_user():
    name = request.json["name"]
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)
