from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.auth.forms import UsersCreationForm, LoginForm
from app.models import Users, db
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UsersCreationForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            confirm_pass = form.confirm_password.data

            if '@employee.com' in email:
                admin = True
            else:
                admin = False
                
            if not confirm_pass == password:
                flash('The passwords do not match')
                return redirect(url_for('auth.signup'))

            user = Users(username, email, password, admin)
            user.save_to_db()
            return redirect(url_for('auth.login'))

        
    return render_template('sign.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method =='POST':
        if form.validate():
            username = form.username.data
            password = form.password.data

            user = Users.query.filter_by(username=username).first()

            print(username, password)

            if user:
                if check_password_hash(user.password, password):
                    print("Logged In")
                    login_user(user)
                    print(user)
                    return redirect(url_for('home'))
                else:
                    flash('Wrong Password')
                    return redirect(url_for('auth.login'))
            else:
                flash('Wrong username')
                return redirect(url_for('auth.login'))



    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))