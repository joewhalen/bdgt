from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from app import config as config

app.config.from_object(config)
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)

class transaction(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    name = db.Column(db.String(80))
    amount = db.Column(db.Float)

    def __init__(self, date, name, amount):
        self.date = date
        self.name = name
        self.amount = amount

from app import views


