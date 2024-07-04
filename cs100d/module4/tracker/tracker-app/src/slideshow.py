import os
import pymysql

f = open("img_data.txt", "r", encoding='utf-8')
lines = f.read().splitlines()
f.close

def login():
    server = "localhost"
    user = "root"
    pwd = "2101"
    db = "img_db"

    conn = pymysql.connect(host=server, user=user, password=pwd, database=db)
    conn.autocommit(True)
    crsr = conn.cursor()
    return crsr, conn

def loadpic(crsr, conn, x):
    line0 = lines[x]
    line1 = lines[x+1]
    line2 = lines[x+2]
    line3 = lines[x+3]
    line4 = lines[x+4]
    img = open(fr'C:\Users\rlsod\rebeccaCS100\cs100d\module4\tracker\tracker-app\src\popdecades\{line0}')
    
    sql = """INSERT INTO img (filename, decade, copyright, info, title, photo) VALUES (%s, %s, %s, %s, %s, %s)"""

    params = (line0, line1, line2, line3, line4, img)

    crsr.execute(sql, params)

    conn.commit()

crsr, conn = login()
for x in range(0, 200, 6):
  loadpic(crsr, conn, x)

