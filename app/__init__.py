from flask import Flask
from flask_socketio import SocketIO
from flask_login import LoginManager
from pymongo import MongoClient
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
mongo = MongoClient('mongodb://user:password@ds135594.mlab.com:35594/blueboard-files')['blueboard-files']
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
socketio = SocketIO(app)

from app import routes, sockets, models