from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://taeheoki:2365@cluster0.nham61w.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'nickname':name_receive,
        'comment':comment_receive
    }
    db.fandoms.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    all_users = list(db.fandoms.find({}, {'_id': False}))
    return jsonify({'fandoms':all_users})

if __name__ == '__main__':
    app.run('0.0.0.0', port=4242, debug=True)