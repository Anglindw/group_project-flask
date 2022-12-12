from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password =  db.Column(db.String(300), nullable=False)
    admin = db.Column(db.String(3), nullable=False)

    def __init__(self, username, email, password, admin):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.admin = admin

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def update_db(self):
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
class Cart(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.JSON(), nullable=False)
    
    def __init__(self, user_id, items):
        self.user_id = user_id
        self.items = items
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def update_db(self):
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
class Items(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    item_name =  db.Column(db.String(100), nullable=False, unique=True)
    item_icon = db.Column(db.String(250), nullable=False)
    item_description = db.Column(db.String(5000), nullable=False)
    item_price = db.Column(db.Float, nullable=False)
    
    def __init__(self, id, item_name, item_icon, item_description, item_price):
        self.id = id 
        self.item_name = item_name
        self.item_icon = item_icon
        self.item_description = item_description
        self.item_price = item_price
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def update_db(self):
        db.session.commit 
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()