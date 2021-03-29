from flask import Flask,render_template,request,redirect,Blueprint,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from admin.routes import admin_bp
from userside.routes import user_bp
app=Flask(__name__)
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)