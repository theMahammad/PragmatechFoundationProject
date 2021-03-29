from flask import render_template,Blueprint
admin_bp = Blueprint('admin',__name__,template_folder='templates')

@admin_bp.route("/adminside")
def index():
    return render_template("admin/index.html")