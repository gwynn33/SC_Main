from flask import Blueprint,redirect,request,url_for,render_template
from flask_login import login_required
from blueprints.database import db
from blueprints.database.database_model import Admin_Account,Temp_User_Informations


tracking_page_bp = Blueprint('tracking_page_bp',__name__)

@tracking_page_bp.route('/permessions/tracking_page')
@login_required
def tracking():
    if Admin_Account.is_admin:     
        if request.method == 'GET':
            temp_user_infos = db.session.query(
                Temp_User_Informations.temp_user_id,
                Temp_User_Informations.temp_user_fullname,
                Temp_User_Informations.temp_user_email,
                Temp_User_Informations.temp_user_Company,
                Temp_User_Informations.temp_user_role,
            )
            return render_template('tracking.html',data=temp_user_infos)
        elif request.method == 'POST':
            return
    else:
        return "Access Denied!",403
        