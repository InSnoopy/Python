from flask import Flask
from flask.globals import request
import psycopg2
from flask.templating import render_template
from flask.json import jsonify
from day12.dao_emp import dao_emp
from day13.DaoStudent import DaoStudent
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("hello.html")

@app.route('/ajax_list', methods=['POST'])
def ajax_list():
    ds = DaoStudent()
    list = ds.selects()
    return jsonify(list=list)


@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    dict = request.get_json()
    ds = DaoStudent()
    list = ds.select(dict['s_id']);
    return jsonify(list=list)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    dict = request.get_json()
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    address = dict['address']
    ds = DaoStudent()
    cnt = ds.insert(s_id, s_name, mobile, address)
    return jsonify(cnt=cnt)


@app.route('/ajax_edit', methods=['POST'])
def ajax_edit():
    dict = request.get_json()
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    address = dict['address']
    ds = DaoStudent()
    cnt = ds.update(s_id, s_name, mobile, address)
    return jsonify(cnt=cnt)

@app.route('/ajax_del', methods=['POST'])
def ajax_del():
    dict = request.get_json()
    e_id = dict['s_id']
    ds = DaoStudent()
    cnt = ds.delete(e_id)
    return jsonify(cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)