import os

basedir = os.path.dirname(os.path.realpath(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '/db/transactions.db'
