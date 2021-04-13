from flask import render_template,Blueprint,redirect,request,flash

from datetime import datetime
import pytz
from werkzeug.utils import secure_filename
from app import db,app
import os,string,random
from .forms import RegistrationForm,LoginForm,FeedbackForm

from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,current_user,logout_user,login_required
from math import ceil,floor,modf


user_bp = Blueprint('user',__name__,template_folder='templates',static_folder='static',static_url_path='/static/userside')
from app import (ContactWays,Details,FAQ,Restaurant,Rules,Subscription,Superiorities,User,AboutUs,Feedback,Like,Dislike)
def usually_used_method():
    return [ceil ,floor,round,modf]
time_zone_Baku = pytz.timezone('Asia/Baku')
month_in_azeri = {
    "01":"Yanvar",
    "02":"Fevral",
    "03" : "Mart",
    "04" : "Aprel",
    "05" : "May",
    "06": "İyun",
    "07": "İyul",
    "08": "Avqust",
    "09" : "Sentyabr",
    "10": "Oktyabr",
    "11" : "Noyabr",
    "12" : "Dekabr"
}
def findAverageRatings(feedback_list):
    sum_taste_rating = 0
    sum_service_rating = 0
    sum_atmp_rating = 0
    averages = [0,0,0]
   
    for feedback in feedback_list:
        if feedback.tasteRating:
            sum_taste_rating+=feedback.tasteRating
        if feedback.serviceRating:
            sum_service_rating+=feedback.serviceRating
        if feedback.atmosphereRating:
            sum_atmp_rating+=feedback.atmosphereRating
    sums = [sum_taste_rating,sum_service_rating,sum_atmp_rating]
    if len(feedback_list):
        averages = [sum /len(feedback_list) for sum in sums]
    averages = [float('%.1f' % average) for average in averages ]
    return averages

        
def getRandomString(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
def save_file_and_return(file,filename,specialName):
    end = 10
    randNum = random.randint(1,end)
    filename= specialName+"_"+filename
    if os.path.exists(os.path.join(app.config['UPLOAD_PATH'],filename)):
        while (os.path.exists(os.path.join(app.config['UPLOAD_PATH'],filename))):
            afterDot = filename[filename.index("."):]
            beforeDot = filename[:filename.index(".")]
            filename = beforeDot+"_"+str(randNum)+afterDot
            end+=1
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
    else:
        file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
    return filename
def secure_and_save_file(data,prefix,class_):
    file = data
    filename = secure_filename(file.filename)
    filename = save_file_and_return(specialName=class_.__name__+"_"+prefix.split()[0],file = file,filename= filename)
    print(filename)
    return filename

def deleteFromUploadFolder(element):
    if(os.path.exists(os.path.join(app.config['UPLOAD_PATH'],element))):
        os.remove(os.path.join(app.config['UPLOAD_PATH'],element))
def deleteCompletely(object_,*args):
    if args:
        for arg in args:
            deleteFromUploadFolder(arg)
    db.session.delete(object_)
    db.session.commit()

@user_bp.route("/",methods = ["GET","POST"])
def index():
    verifiedFeedbacks = Feedback.query.filter_by(verified=True)

    count = 0
    if request.method == "POST":
        allSubscribers = Subscription.query.all()
        for subscriber in allSubscribers:
            if(subscriber.mail == request.form['subscribe']):
                count+=1
        if count==0:
            db.session.add(
                Subscription(mail = request.form['subscribe']
                )
            )
            db.session.commit()
            flash("Abunə oldunuz.Təbriklər!")
        else:
            flash("Siz abunə olmusunuz")
        return redirect("/FAQ")
      
    return render_template("userside/home-page.html",feedbacks = verifiedFeedbacks,Restaurant = Restaurant,User=User,month = month_in_azeri)
@user_bp.route("/restaurants")
def restaurants():
    restaurants = Restaurant.query.all()
    return render_template("userside/restaurants.html",restaurants = restaurants,Feedback = Feedback )
@user_bp.route("/restaurants/profile/<string:rest_slug>")
def restaurantProfile(rest_slug):

    selected_restaurant = Restaurant.query.filter_by(slug=rest_slug).first()
    verified_feedbacks_about_selected = list(filter(lambda item : item.verified==True,selected_restaurant.feedbacks))
    avg_taste,avg_service,avg_atmp = findAverageRatings(verified_feedbacks_about_selected)
   
    return render_template("userside/restaurant_profile.html",selected = selected_restaurant,avg_taste = avg_taste,
    avg_service = avg_service,avg_atmp = avg_atmp,Restaurant = Restaurant,User = User,month = month_in_azeri,
    Like = Like,Dislike = Dislike,Feedback = Feedback,myList = usually_used_method() )

@user_bp.route("/about_us")
def about():
    verifiedAboutUs = AboutUs.query.filter_by(verified=True)
    
    return render_template("userside/about_us.html",allAboutUs = verifiedAboutUs)
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
    verifiedFeedbacks  = Feedback.query.filter_by(verified =True)
    
    return render_template("userside/feedbacks.html",feedbacks  = verifiedFeedbacks,Restaurant = Restaurant,User = User,month = month_in_azeri,Like = Like,Dislike = Dislike )
@user_bp.route("/feedbacks/see_all_content/<string:feedback_slug>")
def showFeedbackDetails(feedback_slug):
    selectedFeedback = Feedback.query.filter_by(slug = feedback_slug).first()

    return render_template("userside/detailed_feedback.html",selected = selectedFeedback,User = User,Restaurant =Restaurant,month = month_in_azeri)
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
                login_user(user)
                flash('Qeydiyyat tamamlandı')
                return redirect("/")
        if log_form.email.data:
            searchedUser = User.query.filter_by(email=log_form.email.data).first()
            if searchedUser:
                if searchedUser.password==log_form.password.data:
                    
                    if log_form.remember.data:
                        remember=True
                    else:
                        remember = False
                    login_user(searchedUser,remember = remember)
                    flash("Təkrar xoş gəldiniz")
                    return redirect("/")
                    
                else:
                    flash("Şifrənizdə yanlışlıq var")
                    return redirect("/login")
            else:
                flash("Sistemdə belə bir istifadəçi yoxdur")
                return redirect("/login")

        
       
    return render_template("userside/login.html",reg_form = reg_form,log_form = log_form)
@user_bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")
@user_bp.route("/add_feedback",methods = ['GET','POST'])
@login_required
def addFeedback():
    form = FeedbackForm()
    filename = None 
    restaurants_ = Restaurant.query.all()
    if request.method == "POST":
        if form.photo.data:
            filename= secure_and_save_file(data=form.photo.data,class_=Feedback,prefix=form.restaurant.data)
        if bool(Restaurant.query.filter_by(name = form.restaurant.data).first()):
            _restaurant_id=Restaurant.query.filter_by(name = form.restaurant.data).first().id
        else:
            _restaurant_id=None
        feedback = Feedback(
            user_id = current_user.get_id(),
            restaurant_name_from_user = form.restaurant.data,
            restaurant_id = _restaurant_id,
            topic = form.topic.data,
            content = form.content.data,
            photo = filename,
            tasteRating  = request.form['taste-rating'],
            serviceRating  = request.form['service-rating'],
            atmosphereRating  = request.form['atmp-rating'],
            time = datetime.now(time_zone_Baku).strftime('%Y-%m-%d | %H:%M:%S')

        )
        db.session.add(feedback)
        db.session.commit()
        return redirect("/")
    return render_template("userside/add_feedback.html",form = form,restaurants = restaurants_)
@user_bp.route("/feedbacks/like/<int:id>")
def likeFeedback(id):
    if Like.query.filter_by(feedback_id=id,user_id=current_user.get_id()).first():
        db.session.delete(Like.query.filter_by(feedback_id=id,user_id=current_user.get_id()).first())
        db.session.commit()
    else:
        db.session.add(
            Like(
            feedback_id=id,
            user_id = current_user.get_id()
        )
        )
        db.session.commit()
    return redirect("/feedbacks")
@user_bp.route("/feedbacks/dislike/<int:id>")
def dislikeFeedback(id):
    if Dislike.query.filter_by(feedback_id=id,user_id=current_user.get_id()).first():
        db.session.delete(Dislike.query.filter_by(feedback_id=id,user_id=current_user.get_id()).first())
        db.session.commit()
    else:
        db.session.add(
            Dislike(
            feedback_id=id,
            user_id = current_user.get_id()
        )
        )
        db.session.commit()
    return redirect("/feedbacks")

    





    
   
      
