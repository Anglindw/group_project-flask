from flask import Flask
from config import Config
from config import Config
from flask_migrate import Migrate
from .models import db, User
from .auth.routes import auth
from flask_login import LoginManager
app = Flask(__name__)


# Init site config class
config_instance = Config()
config = config_instance.__dict__
# Add all fields to site config
app.config["SECRET_KEY"] = config["secret_key"]
for key, value in config['config'].items():
    app.config[key.upper()] = value

login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(auth)

db.init_app(app)
migrate = Migrate(app, db)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

from . import routes
from . import models