from flask import (Flask,render_template,redirect,request,flash)
from flask_login import login_user,logout_user,login_required,LoginManager,UserMixin,current_user
from flask_sqlalchemy import SQLAlchemy

# Built in modules
import os
from datetime import datetime

# Custom modules
from config import username,database_name,password,SECRETE_KEY


# Initialize app & database
app = Flask(__name__)
db = SQLAlchemy(app)

# Authentication code
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


# switch between database storage during production and development using Postgresql database
ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresL//{}:{}@localhost/{}'.format(username,password,database_name)
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] =''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
