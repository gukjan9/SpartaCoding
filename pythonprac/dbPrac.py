from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.vxhks78.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

# # 데이터 넣기
# doc = {'name' : '영희', 'age' : 30}
# db.users.insert_one(doc)

# doc = {'name' : '철수', 'age' : 0}
# db.users.insert_one(doc)

# # 데이터 찾기
# all_users = list(db.users.find({},{'_id':False}))

# # 한 명만 출력
# user = db.users.find_one({})
# print(user)

# # 데이터 업데이트
# db.users.update_one({'name':'영수'},{'$set':{'age':19}})

# # 데이터 삭제
# db.users.delete_one({'name':'영수'})