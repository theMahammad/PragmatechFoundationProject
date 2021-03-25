from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
from sqlalchemy import MetaData
import os


naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['UPLOAD_PATH'] = 'static/uploads'
db = SQLAlchemy(app,metadata= MetaData(naming_convention=naming_convention))

migrate = Migrate()
migrate.init_app(app,db,compare_type=True,render_as_batch = True)
class Foo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    foo_name = db.Column(db.String(50))
    foo_surname  = db.Column(db.String(50))
    foo_email  = db.Column(db.String(50))
class Restaurant(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    rest_logo = db.Column(db.String(50))
    feedbacks = db.relationship("Feedback",backref = "restaurant")

class Feedback(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    restaurant_id  = db.Column(db.Integer,db.ForeignKey('restaurant.id'))
    feedback_content = db.Column(db.String(250))
    rating_star = db.Column(db.Integer)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new",methods = ["GET","POST"])
def addNewFeedback():
    restaurants = Restaurant.query.all()
    if request.method=="POST":
        _fullname = request.form['fullname']
        _email = request.form.get("mail")
        _restaurant_id = int(request.form.get("restaurant-name"))
        _feedback_content = request.form.get("content")
        _rating_star = int(request.form.get('feedback-rating'))
        feedback_ = Feedback(
        fullname = _fullname,
        email = _email,
        feedback_content = _feedback_content,
        restaurant_id=_restaurant_id,
        rating_star= _rating_star
        ) 
        db.session.add(feedback_)
        db.session.commit()
        return redirect("/feedbacks")
    return render_template("new.html",restaurants = restaurants)
@app.route("/feedbacks")
def showAllFeedbacks():
    feedbacks = Feedback.query.all()
    restaurants = Restaurant.query.all()
    return render_template("allFeedbacks.html",feedbacks = feedbacks,restaurants = restaurants ) 

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
# ADD AND SHOW RESTAURANT
@app.route("/add_restaurant",methods = ["GET","POST"])
def addRestaurant():
    filename = None
    restaurants = Restaurant.query.all()
    if request.method=="POST":
        if request.files['restaurant-logo']:
            file = request.files['restaurant-logo']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        restaurant = Restaurant(
            name = request.form.get("restaurant-name"),
            rest_logo = filename
            )
        
        db.session.add(restaurant)
        db.session.commit()
        return redirect("/add_restaurant")
    return render_template("add_restaurant.html",restaurants = restaurants)
@app.route("/add_restaurant/update/<int:id>",methods= ['GET','POST'])
def updateRestaurants(id):
    selected = Restaurant.query.get(id)
    if request.method == "POST":
        file = request.files['restaurant-logo']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        selected.name = request.form.get("restaurant-name")
        selected.rest_logo = filename
        db.session.commit()
        return redirect("/add_restaurant")
    return render_template("updateRestaurant.html",selected = selected)
@app.route("/add_restaurant/delete/<int:id>")
def deleteRestaurant(id):
    selected = Restaurant.query.get(id)
    db.session.delete(selected)
    db.session.commit()
    return redirect("/add_restaurant")
# Show feedbacks about selected restaurant
@app.route('/about/<int:id>')
def showFeedbacks(id):
    selected_rest = Restaurant.query.get(id)
    feedbacks = Feedback.query.all()
    return render_template('aboutRestaurant.html',selected_rest = selected_rest,feedbacks = feedbacks)
if __name__=="__main__":
    app.run(debug=True)
    