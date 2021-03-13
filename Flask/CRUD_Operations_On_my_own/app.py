from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
class Feedback(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    restaurant_name = db.Column(db.String(50))
    feedback_content = db.Column(db.String(250))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new",methods = ["GET","POST"])
def addNewFeedback():
    if request.method=="POST":
        _fullname = request.form.get("fullname")
        _email = request.form.get("mail")
        _restaurant_name = request.form.get("restaurant_name")
        _feedback_content = request.form.get("content")
        feedback_ = Feedback(
        fullname = _fullname,
        email = _email,
        restaurant_name = _restaurant_name,
        feedback_content = _feedback_content
        ) 
        db.session.add(feedback_)
        db.session.commit()
        return redirect("/feedbacks")
    return render_template("new.html")
@app.route("/feedbacks")
def showAllFeedbacks():
    feedbacks = Feedback.query.all()
    return render_template("allFeedbacks.html",feedbacks = feedbacks) 

# Update Operation
@app.route("/update/<int:id>",methods = ["GET","POST"])
def updateFeedback(id):
    feedback=Feedback.query.get(id)
    if request.method=="POST":
        feedback.fullname = request.form.get("fullname")
        feedback.email = request.form.get("mail")
        feedback.restaurant_name = request.form.get("restaurant_name")
        feedback.feedback_content = request.form.get("content")
        db.session.commit()
        return redirect("/feedbacks")
    return render_template("update.html",currentFB= feedback)
# Delete operation
@app.route("/delete/<int:id>")
def deleteFeedback(id):
    fbForDelete=Feedback.query.get(id)
    db.session.delete(fbForDelete)
    db.session.commit()
    return redirect("/feedbacks")
if __name__=="__main__":
    app.run(debug=True)
    