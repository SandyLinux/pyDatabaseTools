import pymongo
from pymongo import MongoClient


client = MongoClient()

db = client.my_db

customers = db.customers.find({'address.building':'1007'})
for i in customers:
    for j in i['grades']:
        if (j['grade'] == 'B'):
            print (j['date'])


cursor = db.customers.find(
    {'grades.score':2}
)
for i in cursor:
    print(i)