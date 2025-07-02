from flask import Blueprint,redirect,request,url_for,render_template

tracking_page_bp = Blueprint('tracking_page_bp',__name__)

@tracking_page_bp.route('/permessions/tracking_page')
def tracking():
    if request.method == 'GET':
        return render_template('tracking.html')
    elif request.method == 'POST':
        return