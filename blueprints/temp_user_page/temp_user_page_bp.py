from flask import Blueprint,request,url_for,redirect,render_template
from flask_login import login_manager,login_required,current_user
from blueprints.database.database_model import Temp_User_Account,Temp_User_Informations

temp_user_page_bp = Blueprint('temp_user_page_bp',__name__)

@temp_user_page_bp.route('/User/page')
@login_required
def user_page():
    try:
        user = current_user.temp_user_id
        user_info = Temp_User_Informations.query.filter_by(temp_user_id=user).first()
        if user_info is None:
            raise Exception("db is not queried successfully !")
        
        return render_template('user_main_page.html',usr=user_info.temp_user_fullname)
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("Error!: ",e)
        return "An error occurred while loading your page.", 500