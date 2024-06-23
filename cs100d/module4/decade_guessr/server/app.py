from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pymysql

app = Flask(__name__)
CORS(app)

# Test API
@app.route('/')
def index():
    return 'Hello World'

# Reset DB
@app.route('/resetdb')
def reset():
    #make sure you modify this connection string to connect to your database, not mine
    server = os.environ['DATAHOST']
    user = os.environ['DATAUSER']
    pwd = os.environ['DATAPWD']
    db = os.environ['DATADATABASE']

    conn = pymysql.connect(host=server, user=user, password=pwd, database=db)
    conn.autocommit(True)
    crsr = conn.cursor()

    # Drop the tables if they already exist
    sql = f'DROP TABLE IF EXISTS `{db}`.`login`;'
    crsr.execute(sql)
    sql = f'DROP TABLE IF EXISTS `{db}`.`user`;'
    crsr.execute(sql)
    # Create the two tables we'll need for our app
    sql = f'CREATE TABLE `{db}`.`user` (`id` INT NOT NULL AUTO_INCREMENT,`login` VARCHAR(255) NULL, PRIMARY KEY (`id`));'
    crsr.execute(sql)
    sql = f'CREATE TABLE `{db}`.`login` (`id` INT NOT NULL AUTO_INCREMENT,`userid` INT NULL,`date` DATETIME, PRIMARY KEY (`id`), FOREIGN KEY (userid) REFERENCES `user`(id));'
    crsr.execute(sql)

    return 'Reset Successful'

#the user's login is being sent via post, in json
@app.route('/login', methods = ['POST'])
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

    #First, check if this user already exists
    sql = 'select id from user where login=%s'
    crsr.execute(sql, (user))
    print('returned ' + str(crsr.rowcount) + ' rows')
    if crsr.rowcount == 0:
        print('adding ' + user)
        crsr.execute('insert into user (login) values (%s)', (user))
        print('adding ' + str(crsr.rowcount) + ' user')
        print('re-executing ' + sql)
        crsr.execute(sql, (user))
    res = crsr.fetchone()
    userid = res[0]
    # Now, add the login information
    # Note, CURRENT_TIMESTAMP is built into MySQL to get the current time
    sql = 'insert into login (userid, `date`) values (%s, CURRENT_TIMESTAMP)'
    crsr.execute(sql, (userid))

    conn.commit()

    # Finally, get the user's login count and the total login count
    sql = 'select count(*) as logins from login where userid=%s'
    crsr.execute(sql, (userid))
    res = crsr.fetchone()
    usercount = res[0]
    sql = 'select count(*) as logins from login'
    crsr.execute(sql)
    res = crsr.fetchone()
    totalcount = res[0]

    return jsonify({'user': user, 'user count':usercount, 'total count':totalcount})

if __name__ == '__main__':
    app.run()