#pip install flask (this might be covered by requirements, do those first (see .env for requirements instructions))
#pip install cryptography???

from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pymysql

app = Flask(__name__)
CORS(app)

#test API
@app.route('/')
def index():
    return 'Hello World'

@app.route('/resetdb')
def reset():
    server = os.environ['DATAHOST']
    user = os.environ['DATAUSER']
    pwd = os.environ['DATAPWD']
    db = os.environ['DATADATABASE']
    
    conn = pymysql.connect(host = server, user = user, password = pwd, database = db)
    conn.autocommit(True)
    crsr = conn.cursor()

    #drop the tables if they already exist
    sql = 'DROP TABLE IF EXISTS `img_db`.`img`;'
    crsr.execute(sql)
    #create the two tables we'll need for our app
    sql = 'CREATE TABLE `img_db`.`img` (`id` varchar(10) AUTO_INCREMENT, `filename` varchar(200), `decade` varchar(200), `copyright` varchar(200), `info` varchar(200), `title` varchar(200), PRIMARY KEY (`id`));'
    crsr.execute(sql)
    

    return 'Reset Successful'

#the user's login is being sent via post, in json
@app.route('/login', methods=['POST'])
def login():
    server = os.environ['DATAHOST']
    user = os.environ['DATAUSER']
    pwd = os.environ['DATAPWD']
    db = os.environ['DATADATABASE']

    conn = pymysql.connect(host=server, user=user, password=pwd, database=db)
    conn.autocommit(True)
    crsr = conn.cursor()

    json = request.get_json()
    user = json['user']

    """
    #first, check if this user already exists
    sql = 'select id from user where login = %s'
    crsr.execute(sql, (user))
    print('returned ' + str(crsr.rowcount) + ' rows')
    if crsr.rowcount == 0:
        print('adding ' + user)
        crsr.execute('insert into user (login) values (%s)', user)
        print('re-executing ' + sql)
        crsr.execute(sql, (user))
    res = crsr.fetchone()
    userid = res[0]
    #now, add the login information
    #note, CURRENT_TIMESTAP is built into MySQL to get the current time
    sql = 'insert into login (userid, `date`) values (%s, CURRENT_TIMESTAMP)'
    crsr.execute(sql, (userid))

    conn.commit()

    #finally, get the user's login count and the total login count
    sql = 'select count(*) as logins from login where userid=%s'
    crsr.execute(sql, (userid))
    res = crsr.fetchone()
    usercount = res[0]
    sql = 'select count(*) as logins from login'
    crsr.execute(sql)
    res = crsr.fetchone()
    totalcount = res[0]
    """
    return jsonify({'id': id, 'filename': filename, 'decade':decade, 'copyright':copyright,'info':info, 'title': title})
    #return jsonify({'user': user, 'user count':usercount, 'total count':totalcount})

if __name__ == '__main__':
    app.run()