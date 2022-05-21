import string
import random
import os
random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))
DEBUG = True

from App.db.conns import return_db
SQLALCHEMY_DATABASE_URI = return_db(1)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key
UPLOAD_FOLDER = 'App/static/img/uploads/'
DOWNLOAD_FOLDER = 'static/downloads/'
DIRECTORY_APP = os.path.abspath(os.getcwd())
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Configuração EMAIL
MAIL_SERVER = 'smtp-rgmsolutions.alwaysdata.net'
MAIL_PORT = 465
MAIL_USERNAME = 'rgmsolutions@alwaysdata.net'
MAIL_PASSWORD = 'rony0608'
MAIL_USE_TLS= False
MAIL_USE_SSL = True