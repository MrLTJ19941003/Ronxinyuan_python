from flask import Blueprint,render_template

indexs = Blueprint('indexs',__name__)

@indexs.route('/')
def index():
    return render_template('index.html')