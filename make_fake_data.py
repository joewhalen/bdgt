from app import db, transaction
from numpy import random
from datetime import datetime

db.create_all()

expenses = ['beer', 'lunch', 'dinner']

for i in range(7):
    num_today =  random.randint(1,4)
    hour_today = 10
    for j in range(num_today):
        new_hr = hour_today + random.randint(5)
        date = datetime(2016,1,19+i,new_hr,random.randint(60),random.randint(60))
        name = expenses[j]
        amount = random.rand()*10
        t = transaction(date,name,amount)
        db.session.add(t)
        hour_today = new_hr

db.session.commit()
