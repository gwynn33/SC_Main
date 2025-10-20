from flask import Blueprint,request,render_template,redirect,url_for
from flask_login import LoginManager,login_required,current_user
from blueprints.database.database_model import Admin_Account
admin_bp = Blueprint('admin_bp',__name__)


@admin_bp.route('/admin')
@login_required
def admin():
    if current_user.is_admin:
        username = current_user.admin_username
        return render_template('admin_page.html',usr=username)
    return "Access Denied !",403
