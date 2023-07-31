from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'random string'
UPLOAD_FOLDER = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
login_manager = LoginManager(app)
login_manager.login_view ='login'
login_manager.login_message_category = 'info'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

from project import main