import tensorflow as tf
from flask import Flask,jsonify,request
import json
app = Flask(__name__)
@app.route('/add',methods=['POST'])
def add():
        x=tf.placeholder(dtype=tf.int32)
        y=tf.placeholder(dtype=tf.int32)
        c=tf.add(x,y)
        print(c)
        data=request.get_json()
        a=data['x']
        b=data['y']
        sess=tf.Session()
        results=tf.add(a,b)
        return jsonify({'sess.run(results)':json.dumps(sess.run(str(results))),'x':a,'y':b})
if __name__ == "__main__":
        app.run(host='0.0.0.0')
