from flask import Blueprint,render_template
userside=Blueprint('user',__name__,template_folder="templates")
@userside.route("/")
def homepage():
    return render_template("user/index.html")