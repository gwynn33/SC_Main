from flask import Blueprint,render_template,request,url_for,redirect,jsonify,make_response
from blueprints.database import db
from flask_login import login_required,current_user
from blueprints.database.database_model import Asset_Existence,Admin_Account,Employee_Asset,Employees
import datetime

scanning_bp = Blueprint('scanning_bp',__name__)


@scanning_bp.route('/scanning',methods=['GET','PUT'])
@login_required
def scanning():
    if Admin_Account.is_admin:
        if request.method == 'GET':
            return render_template('scanning_page.html')

        elif request.method == 'PUT':
            try:
                qr_data = request.get_json()
                if not qr_data:
                    return jsonify({"success":False,"message":"Something Wrong with the Data !"})
                print("raw request : ",request.data)
                print("Content-type :",request.content_type)
                user_id = qr_data.get('employee ID')
                asset_serial_requested = qr_data.get('Serial Code') 


                print("Here is the ID :",user_id)
                print("here is the asset serial :",asset_serial_requested)
                user_data = Asset_Existence.query.filter_by(employee_id=user_id,asset_serial=asset_serial_requested).first()
                if user_data:
                    user_data.scan_counter = user_data.scan_counter + 1 if user_data.scan_counter else 1
                    user_data.last_scan_date = datetime.datetime.now()
                    print("User_found : scan_counter and last_scan_date are Updated!")

                    if not user_data.first_scan_date:
                        user_data.first_scan_date = datetime.datetime.now()
                        print("User_found : first_scan_date is Updated!")

                    if not user_data.existence:
                        user_data.existence = "Exist"
                        print("User_found : Existence Updated!")
                    #database is committed for existing user! 
                    db.session.commit()
                    print("DATA BASE COMMITED !")


                else:
                    new_modification = Asset_Existence(
                        employee_id = user_id,
                        asset_serial = asset_serial_requested,
                        existence = "Exist",
                        first_scan_date = datetime.datetime.now(),
                        last_scan_date = datetime.datetime.now(),
                        scan_counter = 1,
                    )
                    db.session.add(new_modification)
                    print("NEW SCAN RECORD!")
                db.session.commit()
                print("DATA BASE COMMITED !")
                return jsonify({"success":True,"message":"data received ! "})

            except Exception as error:
                print("error" + str(error))
                import traceback
                traceback.print_exc()
                db.session.rollback()
                return jsonify({f"success":False,"error":str(error)})
    else:
        return "Access Denied!",403
            
