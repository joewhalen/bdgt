from app import app, transaction, db 
from flask import render_template, request, jsonify
from datetime import datetime,timedelta

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_expense')
def new_expense():
    return render_template('new_expense.html')

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

@app.route('/weekly_report')
def weekly_report():
    today = datetime.today()
    last_monday = today - timedelta(today.weekday())
    datestring = last_monday.strftime('Week of %b %d')
    return render_template('weekly_report.html', date=datestring)

@app.route('/get_weekly_report')
def get_weekly_report():
    today = datetime.today()
    last_monday = today - timedelta(today.weekday())
    ts = transaction.query.filter(transaction.date <= today, transaction.date >= last_monday).all()

    graph_type = request.args.get('type')
    response = dict(x=[], y=[])

    if len(ts) > 0:
        if graph_type == 'bar':
            lastday_fmt = '%A %m/%d'
            lastday = ts[0].date.strftime(lastday_fmt)
            response['x'].append(ts[0].date.strftime('%a'))
            daysum = 0
            for t in ts:
                if t.date.strftime(lastday_fmt) == lastday:
                    daysum += t.amount
                else:
                    lastday = t.date.strftime(lastday_fmt)
                    response['x'].append(t.date.strftime('%a'))
                    response['y'].append(daysum)
                    daysum = t.amount
        elif graph_type == 'line':
            tot = ts[0].amount
            response['x'].append(int(ts[0].date.strftime('%s'))*1000);
            response['y'].append(tot)
            response['names'] = [ts[0].name]
            for t in ts[1:]:
                tot += t.amount
                response['names'].append(t.name)
                response['x'].append(int(t.date.strftime('%s'))*1000);
                response['y'].append(tot)

    return jsonify(**response)

















