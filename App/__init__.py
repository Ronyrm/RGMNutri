from config import SQLALCHEMY_DATABASE_URI
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate
from googletrans import Translator

from flask_script import Manager

app = Flask(__name__)
db = SQLAlchemy(app,session_options={"autoflush": False})
engine = create_engine(SQLALCHEMY_DATABASE_URI)
translator = Translator()
#try:
#    with engine.connect() as con:
#        sql = open('App\sql\Triggers_sisnutri.sql','r').read()
#        rs = con.execute(sql)
#        print(rs)
#except:
#    pass

migrate = Migrate(app,db)

#manager = Manager(app)
#manager.add_command('db',MigrateCommand)

app.config.from_object('config')
db.init_app(app)


from App.model.atleta import Atleta

from App.routes.iniciarotas import estabelecerotas

estabelecerotas()
db.create_all()