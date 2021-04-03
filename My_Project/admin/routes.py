from flask import render_template,Blueprint,request,redirect,flash
from werkzeug.utils import secure_filename
import os 
from app import db
from app.models import (ContactWays,Details,FAQ,Restaurant,Rules,Subscription,Superiorities,User)
from app import create_app
from admin.forms import SuperioritiesForm,RestaurantsForm



admin_bp = Blueprint('adminPanel',__name__,url_prefix="/adminside",template_folder='templates',static_folder='static',static_url_path='/static/admin')
app = create_app()
@admin_bp.route("")
def index():
    
    return render_template("admin/index.html")
@admin_bp.route("/users")
def users():
    return render_template("admin/users.html",users = User.query.all())
@admin_bp.route("/faq",methods=["GET","POST"])
def faq():
    
    allFaq = FAQ.query.all()
    if request.method=="POST":
        db.session.add(
        FAQ(question = request.form['faq-question'],
        answer = request.form['faq-answer']
        )
    
        )
        db.session.commit()
        return redirect("/adminside/faq")
    return render_template("admin/FAQ.html",allFaq = allFaq)
@admin_bp.route("/faq/delete/<int:id>")
def deleteFaq(id):
   
    db.session.delete(FAQ.query.get(id))
    db.session.commit()
  
    return redirect("/adminside/faq")
@admin_bp.route("/faq/edit/<int:id>",methods = ["GET","POST"])
def editFaq(id):
    selectedFAQ =  FAQ.query.get(id)
    if request.method == "POST":
        selectedFAQ.question = request.form['faq-question']
        selectedFAQ.answer = request.form['faq-answer']
        db.session.commit()
        return redirect("/adminside/faq")
    return render_template("admin/update_faq.html",selected = selectedFAQ)
@admin_bp.route("/subscribers")
def subscribers():
    allSubscribers =  Subscription.query.all()
    return render_template("admin/subscription.html",allSubs = allSubscribers)
@admin_bp.route("/subscribers/delete/<int:id>")
def deleteSubscriber(id):
    db.session.delete(Subscription.query.get(id))
    db.session.commit()
    return redirect("/adminside/subscribers")
@admin_bp.route("/restaurants", methods = ['GET','POST'])
def restaurants():
    filename = None
    forms = RestaurantsForm()
    restaurants = Restaurant.query.all()
    if request.method=="POST":
        if forms.logo.data:
            file = forms.logo.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            restaurant = Restaurant(
            name = forms.name.data,
            logo = filename,
            about = forms.about.data,
            )
        
            db.session.add(restaurant)
            db.session.commit()
            return redirect("/adminside/restaurants")
    return render_template("admin/restaurants.html",restaurants = restaurants,forms = forms)
@admin_bp.route("/restaurants/seeDetails/<int:id>")
def showRestaurantDetails(id):
    return render_template("admin/see_restaurant_details.html",selectedRest = Restaurant.query.get(id))
@admin_bp.route("/restaurants/delete/<int:id>")
def deleteRestaurant(id):
    restaurantForDelete = Restaurant.query.get(id)
    db.session.delete(restaurantForDelete)
    db.session.commit()
    return redirect("/adminside/restaurants")
@admin_bp.route("/restaurants/edit/<int:id>",methods = ['GET','POST'])
def updateRestaurant(id):
    restaurantForUpdate = Restaurant.query.get(id)
    forms = RestaurantsForm()
    if request.method == "POST":
        if forms.logo.data:
            file = forms.logo.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            restaurantForUpdate.name = forms.name.data
            restaurantForUpdate.logo = filename
            restaurantForUpdate.about = forms.about.data
            db.session.commit()
        return redirect('/adminside/restaurants')
    return render_template("admin/update_restaurant.html",selectedRest = restaurantForUpdate,forms = forms)

@admin_bp.route("/rules",methods = ['GET','POST'])
def rules():
   
    rules = Rules.query.all()
    if request.method=="POST": 
        db.session.add(
            Rules(
            title = request.form['rule-title'],
            content = request.form['rule-content']
        ))
        db.session.commit()
        return redirect("/adminside/rules")
    return render_template("admin/rules.html",rules = rules)
@admin_bp.route("/rules/edit/<int:id>",methods = ['GET','POST'])
def editRules(id):
    selectedRule = Rules.query.get(id)
    if request.method=="POST":
        selectedRule.title = request.form['rule-title']
        selectedRule.content = request.form['rule-content']
        db.session.commit()
        return redirect("/adminside/rules")
    return render_template("admin/update_rule.html",selectedRule = selectedRule)
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
            file = forms.img.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
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
    db.session.delete(Superiorities.query.get(id))
    db.session.commit()
    return redirect("/adminside/superiorities")
@admin_bp.route("/superiorities/edit/<int:id>",methods = ['GET','POST'])
def editSuperiority(id):
    selectedSup  = Superiorities.query.get(id)
    forms =  SuperioritiesForm()
    filename = None
    if request.method=="POST":
        if forms.img.data:
            file = forms.img.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
       
        selectedSup.img  = filename
        selectedSup.title = forms.title.data
        selectedSup.content = forms.content.data
        db.session.commit()
        return redirect("/adminside/superiorities")
    return render_template("admin/update_superiority.html",selectedSup = selectedSup,forms = forms)

# CONTACT WAYS CRUD
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
    



    