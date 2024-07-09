from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pymysql

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/data_test')
def data_test():
    conn = pymysql.connect(host='localhost', user='root', password = '2101', database = 'img_db')
    conn.autocommit(True)
    crsr = conn.cursor()

    #crsr.execute("SELECT filename, decade, copyright, info, title FROM img WHERE ID = %s" % rand)
    crsr.execute("SELECT filename, decade, copyright, info, title FROM img WHERE ID = 000")
    result_row = crsr.fetchone()

    return result_row

if __name__ == '__main__':
    app.run()