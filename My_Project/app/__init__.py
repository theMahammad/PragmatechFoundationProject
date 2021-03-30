from flask import Flask,render_template,request,redirect,Blueprint,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from admin.routes import admin_bp
from userside.routes import user_bp
from werkzeug.utils import secure_filename
from sqlalchemy import MetaData
import os

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['UPLOAD_PATH'] = 'static/uploads'

db = SQLAlchemy(app,metadata= MetaData(naming_convention=naming_convention))
migrate = Migrate()
migrate.init_app(app,db,compare_type=True,render_as_batch = True)

app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)
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