from flask import Blueprint,request,url_for,render_template,redirect,jsonify
from blueprints.database import db
from flask_login import login_user,logout_user
from blueprints.database.database_model import Temp_User_Account,Temp_User_feedback



temp_login_bp = Blueprint('temp_login_bp',__name__)

@temp_login_bp.route('/User',methods=['GET','POST'])
def temp_login():
    if request.method == 'GET':
        return render_template('login_page_temp.html')
    elif request.method == 'POST':
        #handeling some beautiful errors ~!
        try:
            #Taking data from the form :)
            user_id = request.form.get('user_id')
            user_password = request.form.get('user_password')
            #verifying
            if not user_id or not user_password:
                  raise ValueError("User_id or user_password is missed !")
            #Querying the database !
            user_account = Temp_User_Account.query.filter_by(temp_user_id=user_id).first()
            if user_account is None:
                raise Exception("Failed to query data !")
            
            #Comparing form values and db values !
            if user_account and user_account.check_temacc_password(user_password):
                login_user(user_account)
                return redirect(url_for('temp_user_page_bp.user_page'))
            else:
                raise ValueError("invalid email or password")
                return redirect(url_for('main_bp.main')) 

        except Exception as err:
            print("Error : ",err)
            import traceback
            traceback.print_exc()
            return redirect(url_for('main_bp.main'))

def logout():
    logout_user()
    return redirect(url_for('main_bp.main'))