from flask import Blueprint,render_template,request

main_bp = Blueprint('main_bp',__name__)

@main_bp.route('/',methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template('main_page.html')
    elif request.method == 'POST':
        return ""