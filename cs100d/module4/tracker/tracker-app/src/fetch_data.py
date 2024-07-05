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
    print(rand)
    strand = str(rand)
    #get all the different variables. what is the most efficient way to do this?
    crsr = conn.cursor()
    crsr.execute("SELECT filename FROM img WHERE ID = %s" % strand)
    this_filename = crsr.fetchall()

    return this_filename

conn = login()
this_filename = grab_slide(conn)
print(str(this_filename))


