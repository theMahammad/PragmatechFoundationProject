from flask import render_template,Blueprint,request,redirect



admin_bp = Blueprint('adminPanel',__name__,url_prefix="/adminside",template_folder='templates',static_folder='static',static_url_path='/static/admin')

@admin_bp.route("")
def index():
    
    return render_template("admin/index.html")
@admin_bp.route("/faq",methods=["GET","POST"])
def faq():
    from app.models import FAQ
    from app import db 
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