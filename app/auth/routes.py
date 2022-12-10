from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.auth.forms import UsersCreationForm
from app.models import Users, db
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/sign', methods=['GET', 'POST'])
def signup():
    form = UsersCreationForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            if '@employee.com' in email:
                admin = 'Yes'
            else:
                admin = 'No'



            print(username, email, password,admin)

            user = Users(username, email, password, admin)

            user.save_to_db()
            #return redirect(url_for('auth.login'))

        
    return render_template('sign.html', form=form)