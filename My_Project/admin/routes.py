from flask import render_template,Blueprint,request,redirect



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
@admin_bp.route("/subscribers")
def subscribers():
    from app import db,Subscription
    allSubscribers =  Subscription.query.all()
    return render_template("admin/subscription.html",allSubs = allSubscribers)
