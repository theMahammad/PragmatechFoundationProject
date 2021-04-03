from flask import render_template,Blueprint,redirect,request,flash
from app.models import (ContactWays,Details,FAQ,Restaurant,Rules,Subscription,Superiorities,User)
from .forms import RegistrationForm
from app import db
user_bp = Blueprint('user',__name__,template_folder='templates',static_folder='static',static_url_path='/static/userside')

@user_bp.route("/",methods = ["GET","POST"])
def index():
    from app import db,Subscription
    count = 0
    if request.method == "POST":
        allSubscribers = Subscription.query.all()
        for subscriber in allSubscribers:
            if(subscriber.mail == request.form['subscribe']):
                count+=1
        if count==0:
            db.session.add(
                Subscription(mail = request.form['subscribe'])
            )
            db.session.commit()
            flash("Abunə oldunuz.Təbriklər!")
        else:
            flash("Siz abunə olmusunuz")
        return redirect("/FAQ")
      
    return render_template("userside/home-page.html")
@user_bp.route("/restaurants")
def restaurants():
    restaurants = Restaurant.query.all()
    return render_template("userside/restaurants.html",restaurants = restaurants)
@user_bp.route("/about_us")
def about():
   return render_template("userside/about_us.html")
@user_bp.route("/rules")
def rules():
    
    rules = Rules.query.all()
    return render_template("userside/rules.html",rules = rules)
@user_bp.route("/FAQ")
def faq():
    FAQS = FAQ.query.all()
    return render_template("userside/faq.html" ,FAQS = FAQS)
@user_bp.route("/partnering")
def partnering():
    return render_template("userside/partnering.html",supers = Superiorities.query.all())
@user_bp.route("/feedbacks")
def feedbacks():
    return render_template("userside/feedbacks.html")
@user_bp.route("/login",methods = ['GET','POST'])
def registration():
    forms = RegistrationForm()
    
    if request.method=="POST":
        user = User(
            fullname=forms.fullname.data,
            email = forms.email.data,
            password = forms.password.data
            )
        registeredUser = User.query.filter_by(email=forms.email.data).first()
        if registeredUser:
            flash("Bu mail sistemdə qeydiyyatdan keçmişdir")
            return redirect("/login")
        else:
            
            db.session.add(user)
            db.session.commit()
            flash("Qeydiyyat tamamlandı")
            return redirect("/")
    return render_template("userside/login.html",forms = forms)
@user_bp.route("/add_feedback")
def addFeedback():
    return render_template("userside/add_feedback.html")
@user_bp.route("/feedback_details")
def showFeedbackDetails():
    return render_template("userside/detailed_feedback.html")

   
      
