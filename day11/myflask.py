from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day11.DaoMember import DaoMember

app = Flask(__name__)

@app.route('/')
@app.route('/mem_list')
def emp_list():
    dm = DaoMember()
    list = dm.selects() 
    return render_template('mem_list.html',list=list)

@app.route('/mem_detail')
def mem_detail():
    a = request.args.get('m_id')
    dm = DaoMember()
    emp = dm.select(a)
    return render_template('mem_detail.html',emp=emp)

@app.route('/mem_edit')
def emp_edit():
    a = request.args.get('m_id')
    dm = DaoMember()
    emp = dm.select(a)
    return render_template('mem_edit.html',emp=emp)

@app.route('/mem_edit_act', methods=['POST'])
def emp_edit_act():
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    dm = DaoMember()
    cnt = dm.update(m_id, m_nm, tel, ymd)
    return render_template('mem_edit_act.html', cnt=cnt)

@app.route('/mem_delete', methods=['POST'])
def emp_delete():
    m_id = request.form['m_id']
    dm = DaoMember()
    cnt = dm.delete(m_id)
    return render_template('mem_delete_act.html',cnt=cnt)

@app.route('/mem_add')
def emp_add():
    return render_template('mem_add.html')

@app.route('/mem_add_act', methods=['POST'])
def emp_add_act():
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    dm = DaoMember()
    cnt = dm.insert(m_id, m_nm, tel, ymd)
    return render_template('mem_add_act.html', cnt=cnt)





if __name__ == '__main__':
    app.run(debug=True)