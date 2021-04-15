from flask import render_template,Blueprint,request,redirect,flash
from werkzeug.utils import secure_filename
import os,string,random
from app import db
from app import app
from app import (ContactWays,Details,FAQ,Restaurant,Rules,Subscription,Superiorities,User,AboutUs,Feedback)

from admin.forms import SuperioritiesForm,RestaurantsForm,FaqForm,RulesForm,AboutUsForm



admin_bp = Blueprint('adminPanel',__name__,url_prefix="/adminside",template_folder='templates',static_folder='static',static_url_path='/static/admin')
rest_name_from_user=None
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
    return filename

def deleteFromUploadFolder(element):
    if(os.path.exists(os.path.join(app.config['UPLOAD_PATH'],element))):
        os.remove(os.path.join(app.config['UPLOAD_PATH'],element))
def deleteCompletely(object_,*args):
    if args:
        for arg in args:
            if arg is not None and arg!="default_rest_logo.png":
                deleteFromUploadFolder(arg)
    db.session.delete(object_)
    db.session.commit()

@admin_bp.route("")
def index():
    feedbacksStillUnverified = Feedback.query.filter_by(verified = False)
    users = User.query.all()
    
    return render_template("admin/index.html",unverifiedFBS = feedbacksStillUnverified,User = User)
@admin_bp.route("/delete_feedback/<int:id>")
def delete_feedback(id):
    feedback = Feedback.query.get(id)
    deleteCompletely(feedback,feedback.photo)
    return redirect("/adminside/feedbacks")
@admin_bp.route("/verify_feedback/<int:id>")
def verify_feedback(id):
    Feedback.query.get(id).verified=True
    db.session.commit()
    return redirect("/adminside/feedbacks")
@admin_bp.route("/unverify_feedback/<int:id>")
def unverify_feedback(id):
    Feedback.query.get(id).verified=False
    db.session.commit()
    return redirect("/adminside/feedbacks")
@admin_bp.route("/see_feedback_details/<int:id>")
def seeFeedbackDetails(id):
    selectedFB = Feedback.query.get(id)
    selectedFB_user_name = User.query.filter_by(id=selectedFB.user_id).first().fullname
    return render_template("admin/see_feedback_details.html",selected = selectedFB,selected_user_name = selectedFB_user_name)
@admin_bp.route("/add_restaurant/<string:rest_name>")
def addRestaurantFromFeedback(rest_name):
    forms = RestaurantsForm()
    restaurants = Restaurant.query.all()
    rest_name_from_user = rest_name
    return render_template("admin/restaurants.html",forms = forms,restaurants = restaurants,rest_name = rest_name_from_user)
@admin_bp.route("/feedbacks")
def showAllFeedbacks():
    return render_template("admin/feedbacks.html",Feedback = Feedback,User = User)
@admin_bp.route("/about_us",methods = ["GET","POST"])
def aboutUs():
    form = AboutUsForm()
    allAboutUs = AboutUs.query.all()
    if request.method=="POST":
        db.session.add(
            AboutUs(content = form.content.data)
            )
        db.session.commit()
        return redirect("/adminside/about_us")
    return render_template("admin/about_us.html",form = form,allAboutUs = allAboutUs)
@admin_bp.route("/about_us/edit/<int:id>",methods = ["GET",'POST'])
def editAboutContent(id):
    selectedContent = AboutUs.query.get(id)
    form = AboutUsForm()
    if request.method=="POST":
        selectedContent.content = form.content.data
        db.session.commit()
        return redirect("/adminside/about_us")
    return render_template("admin/edit_about_content.html",selected = selectedContent,form = form)
    

@admin_bp.route("/about_us/delete/<int:id>")
def deleteAboutContent(id):
    deleteCompletely(AboutUs.query.get(id))
    return redirect("/adminside/about_us")

@admin_bp.route("/about_us/verify/<int:id>")
def  verifyAboutContent(id):
    selected = AboutUs.query.get(id)
    selected.verified = True
    db.session.commit()
    return redirect("/adminside/about_us")
@admin_bp.route("/about_us/unverify/<int:id>")
def  unverifyAboutContent(id):
    selected = AboutUs.query.get(id)
    selected.verified = False
    db.session.commit()
    return redirect("/adminside/about_us")

@admin_bp.route("/users")
def users():
    return render_template("admin/users.html",users = User.query.all())
@admin_bp.route("/users/delete_user/<int:id>")
def deleteUser(id):
    deleteCompletely(User.query.get(id))
    return redirect("/adminside/users")
# ###############################################
# FAQ CRUD OPERATION
@admin_bp.route("/faq",methods=["GET","POST"])
def faq():
    
    allFaq = FAQ.query.all()
    form = FaqForm()
    if request.method=="POST":
        db.session.add(
        FAQ(question = form.question.data,
        answer = form.answer.data
        )
    
        )
        db.session.commit()
        return redirect("/adminside/faq")
    return render_template("admin/FAQ.html",allFaq = allFaq,form = form)
@admin_bp.route("/faq/delete/<int:id>")
def deleteFaq(id):
   
    db.session.delete(FAQ.query.get(id))
    db.session.commit()
  
    return redirect("/adminside/faq")
@admin_bp.route("/faq/edit/<int:id>",methods = ["GET","POST"])
def editFaq(id):
    form = FaqForm()
    selectedFAQ =  FAQ.query.get(id)
    if request.method == "POST":
        selectedFAQ.question = form.question.data
        selectedFAQ.answer = form.answer.data
        db.session.commit()
        return redirect("/adminside/faq")
    return render_template("admin/update_faq.html",selected = selectedFAQ,form = form)
##############################################
# SUBSCRIBER OPERATIONS
@admin_bp.route("/subscribers")
def subscribers():
    allSubscribers =  Subscription.query.all()
    return render_template("admin/subscription.html",allSubs = allSubscribers)
@admin_bp.route("/subscribers/delete/<int:id>")
def deleteSubscriber(id):
    db.session.delete(Subscription.query.get(id))
    db.session.commit()
    return redirect("/adminside/subscribers")
# #######################################################################
# RESTAURANTS  CRUD OPERATIONS
@admin_bp.route("/restaurants", methods = ['GET','POST'])
def restaurants():
    filename = None
    forms = RestaurantsForm()
    restaurants = Restaurant.query.all()
  
    if request.method=="POST":
        if forms.logo.data:
            filename = secure_and_save_file(class_=Restaurant,data=forms.logo.data,prefix=forms.name.data)

        restaurant = Restaurant(
            name = forms.name.data,
            logo = filename,
            about = forms.about.data,
            )
        
        db.session.add(restaurant)
        db.session.commit()
        return redirect("/adminside/restaurants")
    feedbacks_non_with_rest_id = Feedback.query.filter_by(restaurant_id=None)
    for feedback in feedbacks_non_with_rest_id:
            if Restaurant.query.filter_by(name = feedback.restaurant_name_from_user).first():
                feedback.restaurant_id = Restaurant.query.filter_by(name = feedback.restaurant_name_from_user).first().id
    db.session.commit()
    return render_template("admin/restaurants.html",restaurants = restaurants,forms = forms)
@admin_bp.route("/restaurants/seeDetails/<int:id>")
def showRestaurantDetails(id):
    return render_template("admin/see_restaurant_details.html",selectedRest = Restaurant.query.get(id))
@admin_bp.route("/restaurants/delete/<int:id>")
def deleteRestaurant(id):
    object_ = Restaurant.query.get(id)
    deleteCompletely(object_,object_.logo)
    return redirect("/adminside/restaurants")
@admin_bp.route("/restaurants/edit/<int:id>",methods = ['GET','POST'])
def updateRestaurant(id):
    restaurantForUpdate = Restaurant.query.get(id)
    forms = RestaurantsForm()
    filename = restaurantForUpdate.logo
    if request.method == "POST":
        restaurantForUpdate.name = forms.name.data
        if forms.logo.data:
            filename = secure_and_save_file(data = forms.logo.data,prefix=forms.name.data,class_=Restaurant)
            if restaurantForUpdate.logo:
                deleteFromUploadFolder(restaurantForUpdate.logo)
        restaurantForUpdate.logo = filename
        restaurantForUpdate.about = forms.about.data
        db.session.commit()
        return redirect('/adminside/restaurants')
    return render_template("admin/update_restaurant.html",selectedRest = restaurantForUpdate,forms = forms)
# #######################################################################
# RULES  CRUD OPERATIONS
@admin_bp.route("/rules",methods = ['GET','POST'])
def rules():
    forms = RulesForm()
    rules = Rules.query.all()
    if request.method=="POST": 
        db.session.add(
            Rules(
            title = forms.title.data,
            content = forms.content.data
        ))
        db.session.commit()
        return redirect("/adminside/rules")
    return render_template("admin/rules.html",rules = rules,forms = forms)

@admin_bp.route("/rules/edit/<int:id>",methods = ['GET','POST'])
def editRules(id):
    selectedRule = Rules.query.get(id)
    form = RulesForm()
    if request.method=="POST":
        selectedRule.title = form.title.data
        selectedRule.content = form.content.data
        db.session.commit()
        return redirect("/adminside/rules")
    return render_template("admin/update_rule.html",selectedRule = selectedRule,content = str(selectedRule.content), form = form)
@admin_bp.route("/rules/delete/<int:id>")
def deleteRule(id):
    db.session.delete(Rules.query.get(id))
    db.session.commit()
    return redirect("/adminside/rules")
# ##################################################
# SUPERIORITIES CRUD
@admin_bp.route("/superiorities",methods = ["GET","POST"])
def superiority():
    
    forms = SuperioritiesForm()
    supers = Superiorities.query.all()
    filename = None
    if request.method=="POST":
        if forms.img.data:
           filename  = secure_and_save_file(data=forms.img.data,prefix=forms.title.data,class_=Superiorities)
        super = Superiorities(
            img  = filename,
            title = forms.title.data,
            content = forms.content.data

        )    

        db.session.add(super)
        db.session.commit()
        return redirect("/adminside/superiorities")
    return render_template("admin/superiorities.html",supers = supers,restaurants = Restaurant.query.all(),forms = forms)
@admin_bp.route("/superiorities/delete/<int:id>")
def deleteSuperiority(id):
    object_ =  Superiorities.query.get(id)
    deleteCompletely(object_,object_.img)
    return redirect("/adminside/superiorities")
@admin_bp.route("/superiorities/edit/<int:id>",methods = ['GET','POST'])
def editSuperiority(id):
    selectedSup  = Superiorities.query.get(id)
    forms =  SuperioritiesForm()
    filename = None
    if request.method=="POST":
        if forms.img.data:
           filename= secure_and_save_file(forms.img.data,prefix=forms.title.data,class_=Superiorities)
            
        deleteFromUploadFolder(selectedSup.img)
        selectedSup.img  = filename
       
        selectedSup.title = forms.title.data
        selectedSup.content = forms.content.data
        db.session.commit()
        return redirect("/adminside/superiorities")
    return render_template("admin/update_superiority.html",selectedSup = selectedSup,forms = forms)
# #######################################################################
# CONTACT WAYS CRUD OPERATIONS
@admin_bp.route("/contact_ways",methods = ['GET','POST'])
def addAndShowcontact():
    contacts = ContactWays.query.all()
    if request.method=='POST':
        contact = ContactWays(
            facebook = request.form['facebook'],
            twitter = request.form['twitter'],
            instagram = request.form['instagram'],
            youtube = request.form['youtube'],
            gmail  = request.form['gmail'],
            phoneNumber = request.form['phone-number']
        )
        db.session.add(contact)
        db.session.commit()
        return redirect("/adminside/contact_ways")
    return render_template('admin/contact_ways.html',contacts = contacts)
@admin_bp.route('/contact_ways/delete/<int:id>')
def deleteContact(id):
    db.session.delete(ContactWays.query.get(id))
    db.session.commit()
    return redirect("/adminside/contact_ways")
@admin_bp.route("/contact_ways/edit/<int:id>",methods = ['GET','POST'])
def editContact(id):
    selectedContact = ContactWays.query.get(id)
    if request.method=='POST':    
        selectedContact.facebook = request.form['facebook']
        selectedContact.twitter = request.form['twitter']
        selectedContact.instagram = request.form['instagram']
        selectedContact.youtube = request.form['youtube']
        selectedContact.gmail  = request.form['gmail']
        selectedContact.phoneNumber = request.form['phone-number']
        db.session.commit()
        return redirect("/adminside/contact_ways")
    return render_template('admin/update_contact_ways.html',selectedContact = selectedContact)
@admin_bp.route("/partners",methods = ['GET','POST'])
def partners():
    partner_restaurants= Restaurant.query.filter_by(partner_status=True)
    allRestaurants = Restaurant.query.all() 
    if request.method=="POST":
        addedToPartners_id = request.form['part-rest']
        Restaurant.query.filter_by(id=addedToPartners_id).first().partner_status=True
        db.session.commit()
        return redirect("/adminside/partners")
    return render_template("admin/partners.html",partner_restaurants = partner_restaurants,allRestaurants = allRestaurants)
@admin_bp.route("/partners/end_partnering/<int:id>")
def end_partnering(id):
    forEndingPartnering = Restaurant.query.get(id)
    forEndingPartnering.partner_status=False
    db.session.commit()
    return redirect("/adminside/partners")



    