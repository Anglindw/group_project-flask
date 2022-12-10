from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.auth.forms import UserCreationForm
from app.models import User, db
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/sign', methods=['GET', 'POST'])
def signup():
    form = UserCreationForm()
    if request.method == 'POST':
        if form.validate() and "employee.com" in email:
            username = form.username.data
            email = form.email.data
            password = form.password.data
            admin = 'Yes'

            print(username, email, password,admin)

            user = User(username, email, password, admin)

            user.save_to_db()
            #return redirect(url_for('auth.login'))
        elif form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            admin = 'No'

            print(username, email, password, admin)

            user = User(username, email, password, admin)

            user.save_to_db()

        
    return render_template('sign.html', form=form)