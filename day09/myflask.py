from flask import Flask
from flask.globals import request
import psycopg2
from day09.dao_sample import DaoSample
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Python!'

@app.route('/param')
def param():
    a = request.args.get('a','babo')
    return 'param : ' + a

@app.route('/post', methods=['POST'])
def post():
    a = request.form['a']
    return 'post : ' + a

@app.route('/sample')
def sample():
    ds = DaoSample()
    list = ds.selects()
    return str(list)

@app.route('/view')
def view():
    a = "홍길동"
    b = ["바보","천재","미남"]
    c = [
            {'col01':'1','col02':'1','col03':'1'},
            {'col01':'1','col02':'1','col03':'1'},
            {'col01':'1','col02':'2','col03':'3'}
        ]
    return render_template('view.html',value1 = a, value2 = b, value3 = c)

if __name__ == '__main__':
    app.run(debug=True)