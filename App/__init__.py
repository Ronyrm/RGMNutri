from config import SQLALCHEMY_DATABASE_URI
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate
from googletrans import Translator

app = Flask(__name__)
db = SQLAlchemy(app,session_options={"autoflush": False})
engine = create_engine(SQLALCHEMY_DATABASE_URI)
translator = Translator()

migrate = Migrate(app,db)


app.config.from_object('config')
db.init_app(app)


from App.model.atleta import Atleta

from App.routes.iniciarotas import estabelecerotas

estabelecerotas()
db.create_all()