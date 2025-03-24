from flask import render_template, Blueprint

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main.route('/guide')
def guides():
    return render_template('userguide.html')
