from app import app, transaction, db 
from flask import render_template, request
from datetime import datetime

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html',name=name)

@app.route('/<name>_<age>')
def f(name=None, age=None):
    return render_template('name_age.html',name=name,age=age)

@app.route('/add_transaction', methods=['GET','POST'])
def add_transaction():
    if request.method == 'POST':
        name = request.form['expense_name']
        amount = request.form['expense_value']
        date = datetime.now()
        new_transaction = transaction(date, name, amount)
        db.session.add(new_transaction)
        db.session.commit()
    return render_template('index.html')
