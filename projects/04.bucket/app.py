from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.vxhks78.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    bucket_list = list(db.buckets.find({}, {'_id': False}))
    count = len(bucket_list) + 1

    doc = {
        'num': count,  #버킷 등록 시, db에서 특정 버킷을 찾기 위해 'num' 이라는 고유 값 부여
        'bucket' : bucket_receive,
        'done' : 0   #'done' key값을 추가 해 각 버킷의 완료 상태 구분(0 = 미완료, 1 = 완료)
    }
    db.buckets.insert_one(doc)
    return jsonify({'msg': '저장 완료'})
    
@app.route("/bucket", methods=["GET"])
def bucket_get():
    all_buckets = list(db.buckets.find({},{'_id':False}))
    return jsonify({'result': all_buckets})

@app.route("/done", methods=["POST"])
def done_post():
    num_receive = request.form['num_give']
    bucket_receive = request.form['bucket_give']
    done_receive = request.form['done_give']

    print(num_receive, bucket_receive, done_receive)

    db.buckets.update_one({'num':num_receive}, {'$set':{'bucket':bucket_receive}})
    db.buckets.update_one({'num':num_receive}, {'$set':{'done':done_receive}})
    return jsonify({'msg': '완료!!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)