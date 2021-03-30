from flask import render_template,Blueprint,request,redirect,flash
from werkzeug.utils import secure_filename
import os




admin_bp = Blueprint('adminPanel',__name__,url_prefix="/adminside",template_folder='templates',static_folder='static',static_url_path='/static/admin')

@admin_bp.route("")
def index():
    
    return render_template("admin/index.html")
@admin_bp.route("/faq",methods=["GET","POST"])
def faq():
    from app import FAQ,db 
    
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
    from app import FAQ,db
    db.session.delete(FAQ.query.get(id))
    db.session.commit()
  
    return redirect("/adminside/faq")
@admin_bp.route("/faq/edit/<int:id>",methods = ["GET","POST"])
def editFaq(id):
    from app import db,FAQ
    selectedFAQ =  FAQ.query.get(id)
    if request.method == "POST":
        selectedFAQ.question = request.form['faq-question']
        selectedFAQ.answer = request.form['faq-answer']
        db.session.commit()
        return redirect("/adminside/faq")
    return render_template("admin/update_faq.html",selected = selectedFAQ)
@admin_bp.route("/subscribers")
def subscribers():
    from app import db,Subscription
    allSubscribers =  Subscription.query.all()
    return render_template("admin/subscription.html",allSubs = allSubscribers)
@admin_bp.route("/restaurants", methods = ['GET','POST'])
def restaurants():
    from app import Restaurant,db,app
    filename = None
    restaurants = Restaurant.query.all()
    if request.method=="POST":
        if request.files['restaurant-logo']:
            file = request.files['restaurant-logo']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
            restaurant = Restaurant(
            name = request.form.get("restaurant-name"),
            logo = filename,
            about = request.form.get("restaurant-about"),
            )
        
            db.session.add(restaurant)
            db.session.commit()
    return render_template("admin/restaurants.html",restaurants = restaurants)