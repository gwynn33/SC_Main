from flask import Blueprint,request,render_template,redirect,url_for,jsonify
from blueprints.database import db
from flask_login import login_required
from blueprints.database.database_model import Temp_User_Account, Temp_User_Informations,Admin_Account
permession_form_bp = Blueprint('permession_form_bp',__name__)

@permession_form_bp.route('/permessions/register',methods=['GET','POST'])
@login_required
def permessions_form():
    if Admin_Account.admin_id:    
        try:
            if request.method == 'GET':
                return render_template('permession_form.html')
            elif request.method == 'POST':
                data = request.get_json()
                if not data: 
                    return jsonify({'success':False,'error':'No data found!'}),400

                required_fields = {
                    'user_id','user_fullname','user_email',
                    'user_role','user_company','user_password'
                }

                missing = [field for field in required_fields if not data.get(field)]
                if missing: 
                    return jsonify({'success':False,'error':f'Missing fields : {", ".join(missing)}'}),400 #bad request

                user_id = data.get('user_id')
                user_fullname = data.get('user_fullname')
                user_email = data.get('user_email')
                user_role = data.get('user_role')
                user_company = data.get('user_company')
                user_password = data.get('user_password')

                existing_user_data = Temp_User_Informations.query.filter_by(temp_user_id=user_id).first()
                if existing_user_data :
                    return jsonify({'success':False,'error':f'user with this id: {user_id} already exist !'}),409

                user_data = Temp_User_Informations (
                    temp_user_id = user_id,
                    temp_user_fullname = user_fullname,
                    temp_user_email = user_email,
                    temp_user_role = user_role,
                    temp_user_Company = user_company
                )
                user_account = Temp_User_Account(
                    temp_user_id = user_id
                )
                user_account.set_temacc_password(user_password)
                db.session.add(user_data)
                db.session.flush()
                db.session.add(user_account)
                db.session.commit()
                return jsonify({'success':True,'message':'user registred successfully'}),201

        except Exception as error:
            print("ERROR",error)
            import traceback
            traceback.print_exc()
            return jsonify({'success':False,'error': str(error)}),500

    else:
        return "Access denied!",401