import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.vxhks78.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

movie = db.movies2.find_one({'title' : '아저씨'})
print(movie['rank']) 

movie2 = db.movies2.find_one({'title' : '하모니'})
age = movie['age']
all_movies = list(db.movies2.find({'age':age},{'_id':False}))
for m in all_movies :
    print(m['title'])

movie3 = db.movies2.update_one({'title':'부당거래'},{'$set':{'age':'12세 관람가'}})