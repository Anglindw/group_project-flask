import os

basedir = os.environ.get('FLASK_APP')

class Config():
    FLASK_APP = os.environ.get('FLASK_ENV')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATION = False