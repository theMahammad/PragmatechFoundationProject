from flask import Flask,render_template,request,redirect,Blueprint,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from flask_login import UserMixin
from sqlalchemy import MetaData
import os
from flask_login import LoginManager,login_user,current_user,logout_user,login_required



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
class AboutUs(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text)
    verified = db.Column(db.Boolean,default = False)



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



