from flask import Blueprint,redirect,request,url_for,render_template
from flask_login import login_required
from blueprints.database.database_model import Admin_Account

tracking_page_bp = Blueprint('tracking_page_bp',__name__)

@tracking_page_bp.route('/permessions/tracking_page')
@login_required
def tracking():
    if Admin_Account.is_admin:     
        if request.method == 'GET':
            return render_template('tracking.html')
        elif request.method == 'POST':
            return
    else:
        return "Access Denied!",403
        