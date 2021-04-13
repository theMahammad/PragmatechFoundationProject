from flask import Flask,render_template,request,redirect,Blueprint,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from flask_login import UserMixin
from sqlalchemy import MetaData,event
from slugify import slugify
from math import *
import os
from flask_login import LoginManager,login_user,current_user,logout_user,login_required

fromAzeriToEnglish = {
    'ə':"e",
    "ş" :"sh",
    "ı": "i",
    "ü" : "u",
    "ç" : "ch",
    "ğ" : "gh",
    "ö" : "o"

}
def convertation(text,obj):
    
    newText = ''
    text = text.lower()
    temp_text = ''
    class_ = obj.__class__
    for letter in text:
        for key,value in fromAzeriToEnglish.items():
            if(key==letter):
                letter = value
        newText +=letter  
    if class_.query.filter_by(slug = newText).first():
        count = 1
        temp_text  = newText
        while class_.query.filter_by(slug = temp_text).first():
            temp_text = ''
            temp_text = newText+"_"+str(count)
            count+=1
    newText = temp_text
    return newText

    

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['UPLOAD_PATH'] = 'admin/static/admin/uploads'
app.config['SECRET_KEY'] = 'parol'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app,metadata= MetaData(naming_convention=naming_convention))
migrate = Migrate()
migrate.init_app(app,db,compare_type=True,render_as_batch = True)
from flask_sqlalchemy import SQLAlchemy




class Restaurant(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True)
    slug = db.Column(db.String(50),unique=True)
    logo = db.Column(db.String(50),default = "default_rest_logo.png")
    about = db.Column(db.Text)
    feedbacks = db.relationship('Feedback',backref = 'restaurant',lazy = True)
    @staticmethod
    def generate_slug(target,value,oldvalue,initiator):
        
        if value and (not target.slug or value!=oldvalue):
            target.slug=convertation(slugify(value),Restaurant())
db.event.listen(Restaurant.name, 'set', Restaurant.generate_slug, retval=False)
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
    feedbacks = db.relationship('Feedback',backref = 'user',lazy = True)
    likes = db.relationship('Like',backref = 'user',lazy = True)
    dislikes = db.relationship('Dislike',backref = 'user',lazy = True)
class AboutUs(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text)
    verified = db.Column(db.Boolean,default = False)
class Feedback(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    restaurant_name_from_user = db.Column(db.String(100))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    tasteRating = db.Column(db.Integer,nullable = False)
    serviceRating = db.Column(db.Integer,nullable = False)
    atmosphereRating = db.Column(db.Integer,nullable = False)
    topic = db.Column(db.String(100),nullable = False)
    slug = db.Column(db.String(100))
    content = db.Column(db.Text(),nullable = False)
    photo = db.Column(db.String(250))
    verified = db.Column(db.Boolean,default=False)
    time = db.Column(db.String(250))
    likes = db.relationship('Like',backref = 'feedback',lazy = True)
    dislikes = db.relationship('Dislike',backref = 'feedback',lazy = True)
    @staticmethod
    def generate_slug(target,value,oldvalue,initiator):
        
        if value and (not target.slug or value!=oldvalue):
            target.slug=convertation(slugify(value),Feedback())
db.event.listen(Feedback.topic, 'set', Feedback.generate_slug, retval=False)
class PromotionsAboutPartners(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    content = db.Column(db.String(100))
    read_more_url = db.Column(db.String(200))
class Like(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
class Dislike(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

    



    



login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)    
from admin.routes import admin_bp
app.register_blueprint(admin_bp)
from userside.routes import user_bp
app.register_blueprint(user_bp)




