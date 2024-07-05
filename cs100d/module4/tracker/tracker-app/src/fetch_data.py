import os
import pymysql
import random

def login():
    #log into sql
    server = "localhost"
    user = "root"
    pwd = "2101"
    db = "img_db"

    conn = pymysql.connect(host=server, user=user, password=pwd, database=db)
    conn.autocommit(True)
    return conn

def grab_slide(conn):
    #i reallly ought to make all these length counts computerized, but for now i'm just doing them manually
    rand = random.randrange(105)
    
    #get all the different variables. what is the most efficient way to do this?
    sql = """SELECT ID FROM img WHERE ID = %s;""" % rand
    crsr = conn.cursor().execute(sql)
    this_ID = crsr.fetchall()

    return this_ID

conn = login()
this_ID = grab_slide(conn)
print(str(this_ID))


