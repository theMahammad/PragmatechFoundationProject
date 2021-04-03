from flask import Flask,render_template,request,redirect,Blueprint,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from werkzeug.utils import secure_filename
from sqlalchemy import MetaData
import os
from flask_login import LoginManager
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['UPLOAD_PATH'] = 'admin/static/admin/uploads'
app.config['SECRET_KEY'] = 'parol'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app,metadata= MetaData(naming_convention=naming_convention))
migrate = Migrate()
migrate.init_app(app,db,compare_type=True,render_as_batch = True)
db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = "adminPanel.login"
login_manager.init_app(app)
from app.models import (ContactWays,Details,FAQ,Restaurant,Rules,Subscription,Superiorities)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
from admin.routes import admin_bp
app.register_blueprint(admin_bp)
from userside.routes import user_bp
app.register_blueprint(user_bp)



