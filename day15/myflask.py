from flask import Flask
from flask.globals import request
import psycopg2
from flask.templating import render_template
from flask.json import jsonify
from day14.dao_teacher import DaoTe
import time
app = Flask(__name__)


@app.route('/')
@app.route('/thre')
def teacher():
    return render_template("thread.html")

@app.route('/ajax_thread1', methods=['POST'])
def ajax_thread1():
    time.sleep(1);
    a = '1'
    return jsonify(a=a)



@app.route('/ajax_thread2', methods=['POST'])
def ajax_thread2():
    a = '2'
    return jsonify(a=a)




if __name__ == '__main__':
    app.run(debug=True)




