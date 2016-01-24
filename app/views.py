from app import app, transaction, db 
from flask import render_template, request
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/all_transactions')
def all_transactions():
    t = transaction.query.all()
    t = [str(i) for i in t]
    return render_template('show_all.html',transactions=t)
