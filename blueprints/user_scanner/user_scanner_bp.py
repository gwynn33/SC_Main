from flask import Blueprint,request,url_for,redirect,render_template,jsonify
from flask_login import current_user,login_required
from blueprints.database import db
from blueprints.database.database_model import Temp_User_feedback,Temp_User_Account,Asset_Existence
import datetime


user_scanner_bp = Blueprint('user_scanner_bp',__name__)

@user_scanner_bp.route('/User/page/scanner',methods=['GET','PUT'])
@login_required
def user_scanner():
    if Temp_User_Account.is_user:
        if request.method == 'GET':
            return render_template('user_scanner.html')
        elif request.method == 'PUT':
            try:
                data = request.get_json()
                if data.get('type') == 'qr_scanner':
                    if data:
                        print("Data received successfully !")
                        print("raw data : ",request.data)
                        print("content_type : ",request.content_type) #for debugging stuffs !
                    else:
                        return jsonify({"success":False,"error":"Bad request!"})
                    #taking values
                    user_id = data.get('employee ID')
                    serial = data.get('Serial Code')

                    if not user_id or not serial:
                        return jsonify({"success":False,"error":"SOMETHING MISSING!"})

                    print(user_id)
                    print(serial)

                    #querying the database
                    user_data = Asset_Existence.query.filter_by(employee_id=user_id,asset_serial=serial).first()
                    if user_data:
                        #storing some data for debuggin stuffs => to verify if the data is really modified or not !!
                        original_counter_value = user_data.scan_counter
                        original_last_date_value = user_data.last_scan_date

                        #updating values ..!

                        user_data.scan_counter = user_data.scan_counter + 1 if user_data.scan_counter else 1 
                        user_data.last_scan_date = datetime.datetime.now()

                        if not user_data.first_scan_date:
                            user_data.first_scan_date = datetime.datetime.now()

                        if not user_data.existence:
                            user_data.existence = "Exist"

                        if original_counter_value == user_data.scan_counter and \
                         original_last_date_value == user_data.last_scan_date:
                            raise ValueError("DATA IS NOT MODIFIED!")

                        db.session.commit()
                        print("DATABASE COMMITED!")
                        return jsonify({"success":True,"message":"DATABASE UPDATED"})


                    else:
                        #when we scan for the first time case :)
                        user_update = Asset_Existence (
                            employee_id = user_id,
                            asset_serial = serial,
                            existence = "Exist",
                            first_scan_date = datetime.datetime.now(),
                            last_scan_date = datetime.datetime.now(),
                            scan_counter = 1
                        )

                        db.session.add(user_update)
                        db.session.commit()
                        print("NEW SCAN RECORD IS ADDED SUCCESSFULLY!")
                        return jsonify({"success":True,"message":"DATA BASE COMMITED FOR NEW DATA!"})  

                elif data.get('type') == 'form_submit':
                    # handeling fordata :()
                    temperature = data.get('temperature')
                    noise = data.get('noise')
                    desc = data.get('assetstate')
                    empid = data.get('employee ID')
                    serial = data.get('Serial Code')
                    
                    #handling request errors!
                    if not temperature and not noise and not empid and not serial:
                        return jsonify({"success":False,"error":"SOMETHING WRONG DATA NOT REQUESTED!!!"})
                    #Querying the database 
                    data_queried = Temp_User_feedback.query.filter_by(asset_serial = serial ,employee_id = empid ).first()
                    if data_queried:
                        data_queried.asset_temperature = temperature,
                        data_queried.asset_noise = noise,
                        data_queried.asset_state = desc
                        db.session.commit()
                        print("FEEDBACK UPDATED!")
                        return jsonify({"success":True,"message":"FEEDBACK UPDATED SUCCESSFULLY!"})
                    else:
                        unique_case = Temp_User_feedback (
                            employee_id = empid,
                            asset_serial = serial,
                            asset_temperature = temperature,
                            asset_noise = noise,
                            asset_state = desc
                        )
                        db.session.add(unique_case)
                        db.session.commit()
                        print("NEW RECORD ADDED TO FEEDBACK!")
                        return jsonify({"success":True,"message":"NEW FEEDBACK RECORD CREATED SUCCESSFULLY!"})

            except Exception as e:
                import traceback
                db.session.rollback()
                traceback.print_exc()
                print("Error: ",e)
                return jsonify({"success":False,"error":"error! : {}".format(e)})
    else:
        return "Access denied!",403


