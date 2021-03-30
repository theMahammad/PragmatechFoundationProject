from flask import render_template,Blueprint
admin_bp = Blueprint('adminPanel',__name__,template_folder='templates',static_folder='static',static_url_path='/static/admin')

@admin_bp.route("/adminside")
def index():
    return render_template("admin/index.html")