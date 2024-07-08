from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pymysql

app = Flask(__name__)
CORS(app)

#Test API
@app.route('/')
def index():
    return 'WELCOME TO BROWSER 5000'

def login():
    server = os.environ['DATAHOST']
    user = os.environ['DATAUSER']
    pwd = os.environ['DATAPWD']
    db = os.environ['DATADATABASE']

    conn = pymysql.connect(host=server, user=user, password=pwd, database=db)
    conn.autocommit(True)
    crsr = conn.cursor()

    #sql = 'select id from user where login=%s'
    sql = 'select img from img_db where num = id'
    crsr.execute(sql, (user))
    #so how do i see all the properties of crsr, like rowcount?
    print('returned ' + str(crsr.rowcount) + ' rows')

    conn.commit()

if __name__ == '__main__':
    app.run()