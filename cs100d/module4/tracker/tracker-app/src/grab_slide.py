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

def grab_slide(crsr, conn):
    #i reallly ought to make all these length counts computerized, but for now i'm just doing them manually
    rand = random.randrange(105)
    
    #get all the different variables. what is the most efficient way to do this?
    sql = """SELECT column_name FROM img WHERE column_name = %s;"""
    params = rand
    this_column_name = crsr.execute(sql, params)

    sql = """SELECT filename FROM img WHERE column_name = %s;"""
    params = rand
    this_filename = crsr.execute(sql, params)

    sql = """SELECT decade FROM img WHERE column_name = %s;"""
    params = rand
    this_decade = crsr.execute(sql, params)

    sql = """SELECT copyright FROM img WHERE column_name = %s;"""
    params = rand
    this_copyright = crsr.execute(sql, params)

    sql = """SELECT info FROM img WHERE column_name = %s;"""
    params = rand
    this_info = crsr.execute(sql, params)

    sql = """SELECT title FROM img WHERE column_name = %s;"""
    params = rand
    this_title = crsr.execute(sql, params)

    return (this_column_name, this_filename, this_decade, this_copyright, this_info, this_title)

crsr, conn = login()
(this_column_name, this_filename, this_decade, this_copyright, this_info, this_title) = grab_slide(crsr, conn)
print(str(this_column_name) + ' ' + str(this_filename) + ' ' + str(this_decade) + ' ' + str(this_copyright) + ' ' + str(this_info) + ' ' + str(this_title))


