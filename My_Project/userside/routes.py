from flask import render_template,Blueprint,redirect,request,flash
from app.models import (ContactWays,Details,FAQ,Restaurant,Rules,Subscription,Superiorities,User)
from .forms import RegistrationForm,LoginForm
from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,current_user,logout_user,login_required


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
def login():
    reg_form = RegistrationForm()
    log_form  = LoginForm()
    if request.method=="POST":
        if reg_form.fullname.data:
            user = User(
                fullname=reg_form.fullname.data,
                email = reg_form.email.data,
                password = reg_form.password.data
                )
            registeredUser = User.query.filter_by(email=reg_form.email.data).first()
            if registeredUser:
                flash("Bu mail sistemdə qeydiyyatdan keçmişdir")
                return redirect("/login")
            else:
                db.session.add(user)
                db.session.commit()
                flash('Qeydiyyat tamamlandı')
                return redirect("/")
        if log_form.email.data:
            searchedUser = User.query.filter_by(email=log_form.email.data).first()
            if searchedUser:
                if searchedUser.password==log_form.password.data:
                    login_user(searchedUser,remember = log_form.remember.data)
                    flash("Təkrar xoş gəldiniz!")
                    return redirect("/")
                    
                else:
                    flash("Şifrənizdə yanlışlıq var")
                    return redirect("/login")
            else:
                flash("Sistemdə belə bir istifadəçi yoxdur")
                return redirect("/login")

        
       
    return render_template("userside/login.html",reg_form = reg_form,log_form = log_form)

@user_bp.route("/add_feedback")
@login_required
def addFeedback():
    return render_template("userside/add_feedback.html")
@user_bp.route("/feedback_details")
def showFeedbackDetails():
    return render_template("userside/detailed_feedback.html")

   
      
