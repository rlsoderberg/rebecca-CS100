f = open("img_data.txt", "r", encoding='utf-8')
lines = f.read().splitlines()
f.close

import os
import pymysql

def login():
    server = os.environ['DATAHOST']
    user = os.environ['DATAUSER']
    pwd = os.environ['DATAPWD']
    db = os.environ['DATADATABASE']

    conn = pymysql.connect(host=server, user=user, password=pwd, database=db)
    conn.autocommit(True)
    crsr = conn.cursor()

    line0 = lines[x]
    line1 = lines[x+1]
    line2 = lines[x+2]
    line3 = lines[x+3]
    line4 = lines[x+4]

    img = ''

    sql = f'INSERT INTO img (filename, decade, copyright, info, title, photo)
            VALUES ({line0}, {line1}, {line2}, {line3}, {line4}, })'

    crsr.execute(line1, line2, line3, line4, ?, (user))

    conn.commit()

for x in range(0, 200, 5):
  login(x)