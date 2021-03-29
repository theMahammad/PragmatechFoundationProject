from flask import render_template,Blueprint
user_bp = Blueprint('user',__name__,template_folder='templates',static_folder='static',static_url_path='/static/userside')

@user_bp.route("/")
def index():
    return render_template("userside/home-page.html")
@user_bp.route("/restaurants")
def restaurants():
    return render_template("userside/restaurants.html")
@user_bp.route("/about_us")
def about():
   return render_template("userside/about_us.html")
@user_bp.route("/rules")
def rules():
    return render_template("userside/rules.html")