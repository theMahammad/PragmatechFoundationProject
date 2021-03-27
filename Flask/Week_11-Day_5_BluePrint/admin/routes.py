from flask import render_template,Blueprint

dashboard=Blueprint('admin',__name__,static_folder = "static",template_folder="templates",url_prefix="/dashboard")

@dashboard.route("")
def dash():
    return render_template("admin/index.html")
@dashboard.route("/add_feedback")
def newFeedback():
    return render_template("admin/addFeedback.html")