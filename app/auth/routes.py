from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
#from app.auth.forms import UserCreationForm, LoginForm
#from app.models import User, db
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder='auth_templates')