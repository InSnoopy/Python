from flask import Flask
from flask.globals import request
import psycopg2
from flask.templating import render_template
from flask.json import jsonify
from day12.dao_emp import dao_emp
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("hello.html")

@app.route('/ajax', methods=['POST'])
def ajax():
    # data = request.get_json()
    de = dao_emp()
    list = de.selects()
    return jsonify(result = "success", list=list)


@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    dict = request.get_json()
    de = dao_emp();
    list = de.select(dict['e_id']);
    return jsonify(result = "success", list=list)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    dict = request.get_json()
    e_id = dict['e_id']
    e_name = dict['e_name']
    sex = dict['sex']
    addr = dict['addr']
    de = dao_emp();
    cnt = de.insert(e_id, e_name, sex, addr)
    return jsonify(result = "success", cnt=cnt)

@app.route('/ajax_edit', methods=['POST'])
def ajax_edit():
    dict = request.get_json()
    e_id = dict['e_id']
    e_name = dict['e_name']
    sex = dict['sex']
    addr = dict['addr']
    de = dao_emp();
    cnt = de.update(e_id, e_name, sex, addr)
    return jsonify(result = "success", cnt=cnt)

@app.route('/ajax_del', methods=['POST'])
def ajax_del():
    dict = request.get_json()
    e_id = dict['e_id']
    de = dao_emp();
    cnt = de.delete(e_id)
    return jsonify(result = "success", cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)