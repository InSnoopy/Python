from flask import Flask
from flask.globals import request
import psycopg2
from flask.templating import render_template
from flask.json import jsonify
import time
app = Flask(__name__)

@app.route('/')
@app.route('/thre')
def teacher():
    return render_template("three2.html")


if __name__ == '__main__':
    app.run(debug=True)




