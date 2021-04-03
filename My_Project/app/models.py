from app import db
from flask_login import UserMixin
class Restaurant(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    logo = db.Column(db.String(50))
    about = db.Column(db.Text)
    # feedbacks = db.relationship('Restaurant',backref = 'restaurant', lazy = True)
class FAQ(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    question = db.Column(db.String(150))
    answer = db.Column(db.String(250))
class Rules(db.Model):
     id=db.Column(db.Integer,primary_key=True)
     title = db.Column(db.String(150))
     content = db.Column(db.String(250))
class Subscription(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    mail = db.Column(db.String(250))
class Details(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.String(100))
    logo = db.Column(db.String(100))
class Superiorities(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    img = db.Column(db.String(100))
    title = db.Column(db.String(100))
    content = db.Column(db.String(100))

class ContactWays(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    facebook = db.Column(db.String(200))
    instagram = db.Column(db.String(200))
    youtube = db.Column(db.String(200))
    twitter = db.Column(db.String(200))
    phoneNumber = db.Column(db.String(200))
    gmail = db.Column(db.String(200))
class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key = True)
    fullname = db.Column(db.String(50))
    email  = db.Column(db.String(50),unique = True )
    password = db.Column(db.String(50))
 