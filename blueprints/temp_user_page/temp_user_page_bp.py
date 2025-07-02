from flask import Blueprint,request,url_for,redirect,render_template
from flask_login import login_manager,login_required,current_user
from blueprints.database.database_model import Temp_User_Account

temp_user_page_bp = Blueprint('temp_user_page_bp',__name__)

@temp_user_page_bp.route('/User/page')
@login_required
def user_page():
    user = current_user.temp_user_id
    return render_template('user_main_page.html',usr=user)