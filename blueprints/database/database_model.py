from blueprints.database import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin # ich liebe dich you make the current user simple
from datetime import datetime
try:
    class Employees(db.Model):
        __tablename__ = 'employees'
        employee_id = db.Column(db.Integer,primary_key=True)
        admin_id = db.Column(db.Integer,db.ForeignKey('admin_account.admin_id'),nullable=True)
        employee_fullname = db.Column(db.String(30),nullable=False)
        employee_email = db.Column(db.String(60),nullable=False,unique=True)

        def __repr__(self):
            return f"<Employee_fullname : {self.employee_fullname}>"

    class Employee_Asset(db.Model):
        __tablename__ = 'employee_assets'
        asset_serial = db.Column(db.String(30),primary_key=True)
        employee_id = db.Column(db.Integer,db.ForeignKey('employees.employee_id'))
        asset_type = db.Column(db.String(20),nullable=False)
        first_using_date = db.Column(db.Date)
        last_using_date = db.Column(db.Date)

        def __repr__(self):
            return f"<asset_type = {self.asset_type}>"

    class Asset_Existence(db.Model):
        __tablename__ = 'asset_existence'
        employee_id = db.Column(db.Integer,db.ForeignKey('employees.employee_id'),primary_key=True)
        asset_serial = db.Column(db.String(30),db.ForeignKey('employee_assets.asset_serial'),primary_key=True)
        existence = db.Column(db.String(10))
        first_scan_date = db.Column(db.Date)
        last_scan_date = db.Column(db.Date)
        scan_counter = db.Column(db.Integer)

        def __repr__(self): 
            return f"<existence : {self.existence}>"

    class Admin_Account(db.Model,UserMixin): #when we call the current_iser and it's recognized that's because of the Usermixin here !
        __tablename__ = 'admin_account'
        admin_id = db.Column(db.Integer,primary_key=True)
        admin_email = db.Column(db.String(60))
        admin_username = db.Column(db.String(30),nullable=False)
        admin_password = db.Column(db.String(512),nullable=False)
        is_admin = db.Column(db.Boolean,default=True,server_default='1')

        def set_password(self,password):
            #hash the password and store it 
            self.admin_password = generate_password_hash(password)

        def check_password(self,password):
            #checking the password if is it marching the hashed one 
            return check_password_hash(self.admin_password,password)

        def get_id(self):
            return self.admin_id  #ach hadchi !!!!!!!!!!

        def __repr__(self):
            return f"<admin_username = {self.admin_username}>"

    class Temp_User_Informations(db.Model):
        __tablename__ = 'temp_user_informations'
        temp_user_id = db.Column(db.Integer,primary_key=True)
        temp_user_email = db.Column(db.String(60),nullable=False,unique=True)
        temp_user_fullname = db.Column(db.String(30),nullable=False)
        temp_user_get_access_date = db.Column(db.DateTime ,default=datetime.now , nullable=False)
        temp_user_rem_access_date = db.Column(db.Date)
        temp_user_role = db.Column(db.String(20))
        temp_user_Company = db.Column(db.String(30),nullable=False)

        def __repr__(self):
            return f"<temp_user_fullname : {self.temp_user_fullname}>"

    class Temp_User_Account(db.Model,UserMixin):
        __tablename__ = 'temp_user_account'
        temp_user_id = db.Column(db.Integer,db.ForeignKey('temp_user_informations.temp_user_id'),primary_key=True)
        temp_user_password = db.Column(db.String(512),nullable=False)
        is_user = db.Column(db.Boolean,default=True,server_default='1')

        def set_temacc_password(self,password):
            #making the hashed password and store it 
            self.temp_user_password = generate_password_hash(password)

        def check_temacc_password(self,password):
            #checking the password if is it match the hashed one 
            return check_password_hash(self.temp_user_password,password)
        def get_id(self):
            return self.temp_user_id

    class Temp_User_feedback (db.Model):
        __tablename__ = 'temp_user_feedback'
        feedback_id = db.Column(db.Integer,autoincrement=True,primary_key = True)
        asset_serial = db.Column(db.String(30),db.ForeignKey('asset_existence.asset_serial'))
        employee_id = db.Column(db.Integer,db.ForeignKey('employees.employee_id'))
        asset_temperature  = db.Column(db.String(10))
        asset_noise = db.Column(db.String(10))
        asset_state = db.Column(db.String(512),default=None)

        def __repr__(self):
            return f"<asset serial is : {asset_serial}"
except Exception as error:
    print("Error ! :",error)
    import traceback
    traceback.print_exc()



    


