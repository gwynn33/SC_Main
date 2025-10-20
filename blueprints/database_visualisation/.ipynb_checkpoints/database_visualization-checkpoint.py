from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from flask_login import login_required
from blueprints.database import db
from blueprints.database.database_model import Employee_Asset,Admin_Account,Employees,Asset_Existence
from sqlalchemy import and_
import traceback

database_visualization_bp = Blueprint('database_visualization',__name__)

@database_visualization_bp.route('/asset_table',methods=['GET','POST'])
@login_required
def database_visualization():
    if Admin_Account.is_admin:
        if request.method == 'GET':
            employee_assets = db.session.query(
                Employee_Asset.asset_serial,
                Employee_Asset.employee_id,
                Asset_Existence.last_scan_date,
                Asset_Existence.existence,
                Employee_Asset.asset_type,
                Employees.employee_fullname
            ).join(Employees,Employee_Asset.employee_id == Employees.employee_id)\
                .outerjoin(Asset_Existence,
                and_(Employee_Asset.asset_serial == Asset_Existence.asset_serial,
                Employee_Asset.employee_id == Asset_Existence.employee_id))

            return render_template('database_visualization.html',employee_assets=employee_assets)
        
        if request.method == 'POST':
            try:
                formdata = request.get_json()
                
                if not formdata:
                    raise ValueError("DATA NOT REQUESTED!")
                if formdata.get('type') == 'employee_form':
                    #putting API Data into Object
                    dataobj = {
                        'employee_id' : int(formdata.get('employee_id')),
                        'employee_fullname' : formdata.get('employee_fullname'),
                        'employee_email' : formdata.get('employee_email')
                    }

                    if not isinstance(dataobj['employee_id'],int) or dataobj['employee_id'] <= 0  or not dataobj['employee_email'] or not dataobj['employee_email'].strip() or not dataobj['employee_fullname'] or not dataobj['employee_fullname'].strip():
                        return jsonify({"success":False,"error":"FIELD IS MISSED!"})
                    
                    existing_employee = Employees.query.filter_by(employee_id = dataobj['employee_id']).first()
                    
                    if existing_employee:
                        return jsonify({"success":False,"error":"USER IS ALREADY EXIST!"})
                    
                    new_employee = Employees(
                        employee_id = dataobj['employee_id'],
                        employee_fullname = dataobj['employee_fullname'],
                        employee_email = dataobj['employee_email']
                    )                    
                    try:
                        db.session.add(new_employee)
                        db.session.commit()
                        return jsonify({"success":True,"message":"EVERYTHING IS GOOD!"})
                    except Exception as e:
                        db.session.rollback()
                        return jsonify({"success":False,"error":f"SOMETHING WRONG! : {e}"})

                elif formdata.get('type') == 'asset_form':
                    try:
                        assetdata = {
                            'asset_serial' : formdata.get('asset_serial'),
                            'employee_id' : int(formdata.get('employee_id')),
                            'asset_type' : formdata.get('asset_type'),
                            'first_using_date' : formdata.get('first_using_date'),
                            'last_using_date' : formdata.get('last_using_date')
                        }
                        print(assetdata)
                        
                        if not isinstance(assetdata['employee_id'],int) or assetdata['employee_id'] <= 0 or \
                           not assetdata['asset_serial'] or not assetdata['asset_serial'].strip() or \
                           not assetdata['asset_type'] or not assetdata['asset_type'].strip() or \
                           not assetdata['first_using_date']:
                           return jsonify({"success":False,"error":"SOMETHING WRONG! : DATA IS MISSED!"})
                        
                        existing_asset = Employee_Asset.query.filter_by(asset_serial = assetdata['asset_serial'],employee_id = assetdata['employee_id']).first()
                        #verifying if existed!
                        if existing_asset:
                            return({"success":False,"error":"SOMETHING WRONG! : ASSET IS ALREADY EXIST!"})
                        
                        if assetdata['last_using_date']:
                            new_asset = Employee_Asset (
                                asset_serial = assetdata['asset_serial'],
                                employee_id = assetdata['employee_id'],
                                asset_type = assetdata['asset_type'],
                                first_using_date = assetdata['first_using_date'],
                                last_using_date = assetdata['last_using_date']
                            )
                            db.session.add(new_asset)
                            db.session.commit()
                            return jsonify({"success":True,"message":"EVERYTHING IS GOOD!"})
                        else:
                            new_asset = Employee_Asset(
                                asset_serial = assetdata['asset_serial'],
                                employee_id = assetdata['employee_id'],
                                asset_type = assetdata['asset_type'],
                                first_using_date = assetdata['first_using_date']
                            )
                            db.session.add(new_asset)
                            db.session.commit()
                            return({"success":True,"message":"EVERYTHING IS GOOD!"})                            
                    except Exception as e:                 
                        traceback.print_exc()
                        return({"success":False,"error":f"SOMETHING WRONG! : {e}"})

            except Exception as e: 
                traceback.print_exc()
                return jsonify({"success":False,"error":f"ERROR! : {e}"})        


                


