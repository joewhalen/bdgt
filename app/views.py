from app import app
from flask import render_template


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html',name=name)

@app.route('/<name>_<age>')
def f(name=None, age=None):
    return render_template('name_age.html',name=name,age=age)
