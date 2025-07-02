from flask import Blueprint,request,render_template,redirect,url_for
from flask_bcrypt import Bcrypt
from flask_login import login_user,logout_user 
from blueprints.database.database_model import Admin_Account
from blueprints.database import db
import flash


login_bp = Blueprint('login_bp',__name__)
logout_bp = Blueprint('logout_bp',__name__)

@login_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login_page.html')

    elif request.method == 'POST':
        
        #taking the values from the form 
        email = request.form.get('email')
        password = request.form.get('password')
        
        #query the DB 
        admin = Admin_Account.query.filter_by(admin_email=email).first()
        #checking 
        if admin and admin.check_password(password):
            login_user(admin)
            return redirect(url_for('admin_bp.admin'))   
        else: 
            print("Invalid email or password !")
            return(redirect(url_for('login_bp.login')))

        return(redirect(url_for('main_bp.main')))


@logout_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_bp.main'))