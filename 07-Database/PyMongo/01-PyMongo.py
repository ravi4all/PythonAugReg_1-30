from pymongo import MongoClient

def get_db():
    client = MongoClient('localhost:27017')
    db = client.python_db
    return db

def add_user(db):
    db.users.insert({"name" : "Mohan", "age" : 24, "salary" : 25000})

def findUser(db):
    return db.users.find()
    # db.users.find({"name" : "Shyam"})

db = get_db()
add_user(db)
# print(findUser(db))
data = findUser(db)
for d in data:
    print(d)
