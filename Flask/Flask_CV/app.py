from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  ='sqlite:///data.db'
db= SQLAlchemy(app)
class Profile(db.Model):
    id = db.Column(db.Integer,primary_key = True) 
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(50))
    adress = db.Column(db.String(50))
    email_adress = db.Column(db.String(50))
    skills = db.relationship("Skills",backref="profile",lazy = True)   
    education = db.relationship("Education",backref="profile",lazy = True)   
    experience = db.relationship("Education",backref="profile",lazy = True)
class Skills(db.Model):
    id = db.Column(db.Integer,primary_key = True)  
    name = db.Column(db.String(50))
    star = db.Column(db.Integer)
    profile_id = db.Column(db.Integer,db.ForeignKey("profile.id"),nullable = False) 
class Education(db.Model):
    id = db.Column(db.Integer,primary_key = True)  
    degree = db.Column(db.String(50))
    place_name = db.Column(db.String(50))
    years = db.Column(db.String(50))
    profile_id = db.Column(db.Integer,db.ForeignKey("profile.id"),nullable = False) 
class WorkExperience(db.Model):
    id = db.Column(db.Integer,primary_key = True) 
    position = db.Column(db.String(50))
    company_name = db.Column(db.String(50))
    years = db.Column(db.String(50))
    profile_id = db.Column(db.Integer,db.ForeignKey("profile.id"),nullable = False) 
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/add_resume",methods = ["GET","POST"])
def addResume():
    return render_template("add_resume.html")
@app.route("/show_resumes/<int:id>")
def showSpecificResume(id):
    id = id
    return render_template("resume.html",id = id)
if __name__=="__main__":
    app.run(debug=True)