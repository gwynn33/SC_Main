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
from blueprints.database import db 
from flask import Flask,session
from flask_migrate import Migrate
from flask.cli import with_appcontext
from flask_login import LoginManager
import secrets
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
    
    # ach hadchi ?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    @login_manager.user_loader
    def load_user(user_id):
        try:
            user_id = int(user_id)
        except ValueError:
            return None
        
        admin = Admin_Account.query.get(user_id) ## maybe we gonna cast it based on it's type
        if admin: 
            return admin
        
        temp_user = Temp_User_Account.query.get(user_id)
        if temp_user:
            return temp_user
        
        return None

    
    #routes
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


    #migrate
    migrate = Migrate(app,db)
    ##Cli commands
    @app.cli.command('create-employee_asset')
    @click.argument('serial')
    @click.argument('emp_id',type=int)
    @click.argument('asset_t')
    @click.argument('fdate')
    @click.option('--ldate',default=None,help='last_using_date of asset')
    def create_employee_asset(serial,emp_id,asset_t,fdate,ldate):
        existing_employee_asset = Employee_Asset.query.filter_by(asset_serial=serial,employee_id=emp_id).first()
        if existing_employee_asset:
            click.echo(f"this asset is Already exits/used by {emp_id}")
            return
        assets = Employee_Asset(
            asset_serial=serial,
            employee_id=emp_id,
            asset_type=asset_t,
            first_using_date=fdate,
            last_using_date=ldate,
        )

        db.session.add(assets)
        db.session.flush()


        if not ldate or ldate.strip() == "":
            assets_to_existence_check = Asset_Existence (
                employee_id = emp_id,
                asset_serial = serial
            )
            db.session.add(assets_to_existence_check)
            click.echo(f"Asset {asset_t} is Curently with {emp_id}")
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