from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.vxhks78.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

doc = {
    'name' : '영수',
    'age' : 24
}

db.users.insert_one(doc)