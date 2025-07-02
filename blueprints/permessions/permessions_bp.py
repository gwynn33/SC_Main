from flask import Blueprint,render_template,url_for,redirect,request
from flask_login import login_required
from blueprints.database.database_model import Admin_Account

permessions_bp = Blueprint('permessions_bp',__name__)

@permessions_bp.route('/permessions',methods=['GET','POST'])
@login_required
def permessions():
    if Admin_Account.is_admin:    
        if request.method == 'GET':
            return render_template('permession_page.html') 
        elif request.method == 'POST':
            return ""
    else:
        return "Access Denied!",403