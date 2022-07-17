import pymongo

client = pymongo.MongoClient("mongodb+srv://arshewin:mongodb12@cluster0.wckow.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)


d = {
    "name": "arshewin",
    "email": "arshewin.l.com",
    "surname": "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)