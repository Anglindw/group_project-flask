from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password =  db.Column(db.String(300), nullable=False)

    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()