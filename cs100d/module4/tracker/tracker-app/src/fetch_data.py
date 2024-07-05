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
    crsr = conn.cursor()
    return crsr, conn

def grab_slide(crsr):
    #i reallly ought to make all these length counts computerized, but for now i'm just doing them manually
    rand = random.randrange(105)
    
    #get all the different variables. what is the most efficient way to do this?
    sql = """SELECT column_name FROM img WHERE column_name = %s;""" % rand
    params = rand
    this_column_name = crsr.fetchall(sql)

    return this_column_name

crsr = login()
this_column_name = grab_slide(crsr)
print(str(this_column_name))


