from flask import Blueprint,render_template,url_for,redirect,request

permessions_bp = Blueprint('permessions_bp',__name__)

@permessions_bp.route('/permessions',methods=['GET','POST'])
def permessions(): 
    if request.method == 'GET':
        return render_template('permession_page.html') 
    elif request.method == 'POST':
        return ""