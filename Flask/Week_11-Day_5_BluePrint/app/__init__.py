from flask import Flask,redirect,url_for,render_template,request,url_for,Blueprint
from admin.routes import dashboard
from user.routes import userside
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
db=SQLAlchemy(app)
migration = Migrate(app,db)
from app import models
app.register_blueprint(dashboard)
app.register_blueprint(userside)
