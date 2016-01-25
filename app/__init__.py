from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from app import config as config

app.config.from_object(config)
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

    def __str__(self):
        return self.date.strftime('%a %m/%d')+self.name+' $%.2f'%self.amount

from app import views


