from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'
db = SQLAlchemy(app)
class FAQ(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    question = db.Column(db.String(250))
    answer = db.Column(db.String(250))
class Rule(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(250))
    content = db.Column(db.String(250))
class AboutUs(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(250))
    content = db.Column(db.String(250))
class Restaurant(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    about = db.Column(db.String(250))
    address = db.Column(db.String(100))
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    fullname = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    password = db.Column(db.String(50))
class Partnershipping(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    company_name = db.Column(db.String(50))
    title = db.Column(db.String(50))
    content = db.Column(db.String(250))
    phone_number = db.Column(db.String(255))
class Subscription(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    mail_adress = db.Column(db.String(50))

@app.route("/")
def homePage():
    return render_template("app/home-page.html")
if __name__=="__main__":
    app.run(debug=True)
