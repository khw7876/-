from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import certifi
import hashlib
import datetime
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.alyd7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.sparta


@app.route('/')
def home():
    return render_template('login.html')


@app.route("/login/save", methods=["POST"])
def sign_up():
    id_recieve = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    docu = {
        'id': id_recieve,
        'pw': pw_hash}

    db.mydb.insert_one(docu)
    return jsonify({'result': 'success'})

@app.route('/login', methods=['POST'])
def login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    result = db.mydb.find_one({'id':id_receive, 'pw': pw_hash})

    if result is not None:
        payload = {
            'id' : id_receive,
            'exp' : datetime.utcnow() + timedelta(seconds=60 * 30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'success', 'token': token})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)