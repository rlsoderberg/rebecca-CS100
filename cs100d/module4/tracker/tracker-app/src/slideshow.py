from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pymysql

app = Flask(__name__)
CORS(app)

f = open("img_data.txt", "r", encoding='utf-8')
lines = f.read().splitlines()
f.close

def login():
    conn = pymysql.connect(host='localhost', user='root', password='2101', database='img_db')
    conn.autocommit(True)
    crsr = conn.cursor()
    return crsr, conn

crsr, conn = login()

def loadpic():
    line0 = lines[x]
    line1 = lines[x+1]
    line2 = lines[x+2]
    line3 = lines[x+3]
    line4 = lines[x+4]
    img = open(f'C:\Users\rlsod\rebeccaCS100\cs100d\module4\tracker\tracker-app\src\popdecades\{line0}', 'rb', encoding='utf-8')


    sql = f'INSERT INTO img (filename, decade, copyright, info, title, photo) VALUES ({line0}, {line1}, {line2}, {line3}, {line4}, {img});'


    crsr.execute(sql, 'root')


    conn.commit()

login()
for x in range(0, 200, 6):
  loadpic()

