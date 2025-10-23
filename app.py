from blueprints.database.database_model import Admin_Account,Employees,Employee_Asset,Temp_User_Account,Asset_Existence,Temp_User_feedback
from blueprints.main_page.main_bp import main_bp
from blueprints.login_page.login_bp import login_bp
from blueprints.login_page.login_bp import logout_bp
from blueprints.admin_page.admin_bp import admin_bp
from blueprints.qr_scanner.scanning_bp import scanning_bp
from blueprints.permessions.permessions_bp import permessions_bp
from blueprints.tracking_page.tracking_page_bp import tracking_page_bp
from blueprints.permessions_form.permession_form import permession_form_bp
from blueprints.temp_login_user.temp_login_bp import temp_login_bp
from blueprints.temp_user_page.temp_user_page_bp import temp_user_page_bp
from blueprints.temp_login_user.temp_login_bp import temp_logout_bp
from blueprints.user_scanner.user_scanner_bp import user_scanner_bp
from blueprints.database_visualisation.database_visualization import database_visualization_bp
from blueprints.database import db 
from flask import Flask,session
from flask_migrate import Migrate
from flask.cli import with_appcontext
from flask_login import LoginManager
import secrets
from datetime import datetime
import click




def create_app():
    app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gwynn:gwynnistrash12%40%40@localhost/syngenta_connect'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #Session Key 
    app.config['SECRET_KEY'] = secrets.token_urlsafe(32)
    
    #linking the app with the database
    db.init_app(app)
    
    #login Manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main_bp.main'
    login_manager.login_message = "Please log in to access this page !"
    
    # this is a function which separete between auth
    @login_manager.user_loader
    def load_user(user_id):
        try:
            user_id = int(user_id)
        except ValueError:
            return None
        
        admin = Admin_Account.query.get(int(user_id))
        """maybe we gonna cast it based on it's type , i still need to modify it in future (type distinction)"""
        if admin: 
            return admin
        
        temp_user = Temp_User_Account.query.get(int(user_id))
        if temp_user:
            return temp_user
        
        return None
        
        
    #bleuprints registrations
    app.register_blueprint(main_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(permessions_bp)
    app.register_blueprint(scanning_bp)
    app.register_blueprint(tracking_page_bp)
    app.register_blueprint(permession_form_bp)
    app.register_blueprint(temp_login_bp)
    app.register_blueprint(temp_user_page_bp)
    app.register_blueprint(temp_logout_bp)
    app.register_blueprint(user_scanner_bp)
    app.register_blueprint(database_visualization_bp)


    #migrate
    migrate = Migrate(app,db)
    #Cli commands to avoid sql injection (maybe!)
    # COMMAND WITH NO SENS STILL NEED REVISION :()
    @app.cli.command('set-admin')
    @click.argument('identity',type=int)
    @with_appcontext
    def set_admin(identity):
        try:
            unique_admin = Admin_Account.query.first()
            if not  unique_admin:
                raise ValueError("NO ADMIN FOUND!")
            updated_table = Employees.query.filter_by(employee_id = identity).update({
                Employees.admin_id : unique_admin.admin_id
            })
            db.session.commit()
            if updated_table:
                click.echo("THE DUMB COMMAND WORKS!")
            else:
                raise ValueError("TABLE IS NOT UPDATED !")
        except Exception as e:
            click.echo("Something Wrong!{}".format(e))

    #command to activate admin account!
    @app.cli.command('activate-admin')
    @with_appcontext
    def activate_admin():
        update_admin = Admin_Account.query.filter(Admin_Account.is_admin == None).update({
            Admin_Account.is_admin : True
        })
        db.session.commit()
        click.echo("accounts are activated !")
    #command to activate user account
    @app.cli.command('activate-user')
    @click.argument('user_id',type=int)
    @with_appcontext
    def activate_user(user_id):
        if user_id:
            account_activation  = Temp_User_Account.query.filter_by(temp_user_id=user_id).first()
            if account_activation:
                account_activation.is_user = True
                db.session.commit()
                click.echo(f"User <{user_id}> is activated !")
            else:
                click.echo(f"There is no account with this user ID <{user_id}>")
        else:
            click.echo("SOMETHING WENT WRONG VRIFY YOUR INPUT !")
            """that's means account not found probably or something wrong with Querying the DB it still needs revision """ 
    
    #COMMAND TO DEACTIVATE USER ACCOUNT 
    @app.cli.command('deactivate-user')
    @click.argument('user_id',type=int)
    @with_appcontext
    def deactivate_user(user_id):
        if user_id:
            account_deactivation = Temp_User_Account.query.filter_by(temp_user_id=user_id).first()
            if account_deactivation:
                account_deactivation.is_user = None
                db.session.commit()
                click.echo(f"User <{user_id}> is  deactivated !")
            else:
                click.echo(f"There is no account with this user ID <{user_id}>")
        else:
            confirm = click.confirm("DO YOU REALLY WANT TO DEACTIVATE ALL THIS ACCOUNTS?" ,abort=True)
            remove_access_from_all = Temp_User_Account.query.update({Temp_User_Account.is_user : None})
            db.session.commit()
            click.echo("ALL THE USERS ACCOUNTS ARE DEACTIVATED !")


    #command to deactivate admin accounts / specified one or all of them for (security reasons) !!
    @app.cli.command('deactivate-admin')
    @click.option('--email',default=None,help='this option for a specifique admin.')
    @with_appcontext
    def deactivate_admin(email):
        if email:
            admin = Admin_Account.query.filter_by(admin_email=email).first()
            if admin:
                admin.is_admin = None
                db.session.commit()
                click.echo("Admin is deactivated successfully !")
            else:
                click.echo(f"No admin found with this email : {email}")
        else:
            confirmation = click.confirm("DO YOU REALLY WANT TO DEACTIVATE ALL OF THOSE ACCOUNTS?",abort=True)
            remove_access_from_all = Admin_Account.query.update({Admin_Account.is_admin : None})
            db.session.commit()
            click.echo("all the admins are deactivated !")

    #Employee Creation 
    @app.cli.command('create-employee_asset')
    @click.argument('serial')
    @click.argument('emp_id',type=int)
    @click.argument('asset_t')
    @click.argument('fdate')
    @click.option('--ldate',default=None,help='last_using_date of asset')
    #main function
    def create_employee_asset(serial,emp_id,asset_t,fdate,ldate):
        #function to verify the date format
        def validate_date(date_str,fieldname):
            if not date_str:
                return None
            
            try:
                return datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                click.echo(f"ERROR : {fieldname} must be in YYYY-MM-DD format")
                return False
            
        validate_fdate = validate_date(fdate,'first_scan_date')
        if validate_fdate is False:
            return

        validate_ldate = validate_date(ldate,'last_scan_date')
        if validate_ldate is False:
            return
        
        #looking for existing data 
        existing_employee_asset = Employee_Asset.query.filter_by(asset_serial=serial,employee_id=emp_id).first()
        if existing_employee_asset:
            click.echo(f"this asset is Already exist/used by {emp_id}")
            return
        #if not adding new data to employee_asset
        assets = Employee_Asset(
            asset_serial=serial,
            employee_id=emp_id,
            asset_type=asset_t,
            first_using_date=validate_fdate,
            last_using_date=validate_ldate,
        )
        #add values to db
        db.session.add(assets)
        db.session.flush()

        #verifying last_scan_date
        if not validate_ldate:
            assets_to_existence_check = Asset_Existence (
                employee_id = emp_id,
                asset_serial = serial
            )

            asset_feedback = Temp_User_feedback(
                employee_id = emp_id,
                asset_serial = serial
            )

            db.session.add(assets_to_existence_check)
            db.session.flush()
            db.session.add(asset_feedback)
            click.echo(f"Asset {asset_t} is Curently with {emp_id}")
            click.echo("important informations also sent to feedback table")
        else:
            click.echo(f"Asset {asset_t} was returned by {emp_id} in {ldate}")

        db.session.commit()
        click.echo("asset is added successfully")

        
    #cli command to add an Employee
    @app.cli.command('create-employee')
    @click.argument('idn',type=int)
    @click.argument('first_name')
    @click.argument('last_name')
    @click.argument('email')
    def create_employee(idn,first_name,last_name,email):
        existing_employee = Employees.query.filter_by(employee_id=idn).first()
        if existing_employee:
            click.echo(f'employee {first_name}  {last_name} is already exist')
        full_name = f'{first_name} {last_name}'
        employee = Employees(
            employee_id = idn,
            employee_fullname = full_name,
            employee_email = email
        )
        db.session.add(employee)
        db.session.commit()
        click.echo(f'Employee {full_name} is created successfully')
    
    #cli command to add a hashable password to admin Account
    @app.cli.command()
    @click.argument('username')
    @click.argument('password')
    @click.option('--email',prompt='admin email',help='admin email Address')
    @click.option('--idn',prompt='admin id',help='Admin identifier',type=int)
    @with_appcontext
    def create_admin(username,password,email,idn):
        #we are going to create admin_account
        existing_admin = Admin_Account.query.filter_by(admin_username=username,admin_id=idn).first()
        if existing_admin:
            click.echo(f'Admin {username} is already exist ! ')
            return
        
        admin = Admin_Account (
            admin_username=username,
            admin_email=email,
            admin_id=idn
        )

        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
        click.echo(f"Admin User {username} Created successfully")

    return app

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5555',debug=True)
