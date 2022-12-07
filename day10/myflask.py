from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day10 import dao_emp
from day10.dao_emp import dao_emp

app = Flask(__name__)

@app.route('/')
@app.route('/emp_list')
def emp_list():
    de = dao_emp()
    list = de.selects() 
    return render_template('emp_list.html',list=list)

@app.route('/emp_detail')
def emp_detail():
    a = request.args.get('e_id')
    de = dao_emp()
    emp = de.select(a)
    return render_template('emp_detail.html',emp=emp)

@app.route('/emp_edit')
def emp_edit():
    a = request.args.get('emp_edit')
    de = dao_emp()
    emp = de.select(a)
    return render_template('emp_edit.html',emp=emp)

@app.route('/emp_edit_act', methods=['POST'])
def emp_edit_act():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    de = dao_emp()
    cnt = de.update(e_id, e_name, sex, addr)
    return render_template('emp_edit_act.html', cnt=cnt)

@app.route('/emp_delete', methods=['POST'])
def emp_delete():
    e_id = request.form['e_id']
    de = dao_emp()
    cnt = de.delete(e_id)
    return render_template('emp_delete_act.html',cnt=cnt)

@app.route('/emp_add')
def emp_add():
    return render_template('emp_add.html')

@app.route('/emp_add_act', methods=['POST'])
def emp_add_act():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    de = dao_emp()
    cnt = de.insert(e_id, e_name, sex, addr)
    return render_template('emp_add_act.html', cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)
