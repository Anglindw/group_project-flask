from app import app
from flask import redirect, render_template, url_for, flash
from flask_login import current_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')