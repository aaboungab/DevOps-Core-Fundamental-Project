from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:00@35.246.4.57/ReviewProject'
app.config['SECRET_KEY'] = 'Mystic'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

from application import routes
