from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

@app.route('/')
def home():
    return render_template('2nd.html')

@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phonenumber_receive = request.form['phonenumber_give']

    order = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phonenumber': phonenumber_receive
    }
    db.reviews.insert_one(order)
    return jsonify({'result':'success', 'msg': '준비 완료!'})



@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.reviews.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)