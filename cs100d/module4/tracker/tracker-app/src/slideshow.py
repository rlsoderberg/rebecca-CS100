import os
import pymysql

#read image data
data_file = open("img_data.txt", "r", encoding='utf-8')
lines = data_file.read().splitlines()
data_file.close()

#log into sql (really should be using .env, but the import was having some weird problem)
def login():
    server = "localhost"
    user = "root"
    pwd = "2101"
    db = "img_db"

    conn = pymysql.connect(host=server, user=user, password=pwd, database=db)
    conn.autocommit(True)
    crsr = conn.cursor()
    return crsr, conn

#load image data into SQL
def loadpic(crsr, conn, x):
    #assign variables to different lines of data file
    line0 = lines[x]
    print('line 0:'+line0)
    line1 = lines[x+1]
    print('line 1:'+line1)
    line2 = lines[x+2]
    print('line 2:'+line2)
    line3 = lines[x+3]
    print('line 3:'+line3)
    line4 = lines[x+4]
    print('line 4:'+line4)
    
    #make an image path, using the filename (first line of every five lines of data file)
    #img_path = fr'C:\Users\rlsod\rebeccaCS100\cs100d\module4\tracker\tracker-app\src\popdecades\{img_filename}'

    #read binary data from image file at this image path
    #img_file = open(img_path, 'rb')
    #img_data = img_file.read()
    #img_file.close()
    
    #sql statement to insert variables and image data
    sql = """INSERT INTO img (filename, decade, copyright, info, title) VALUES (%s, %s, %s, %s, %s)"""

    #define params and then execute with them
    params = (line0, line1, line2, line3, line4)

    crsr.execute(sql, params)

    conn.commit()

crsr, conn = login()
#do the loop... every 6 times? do i need to make a placeholder for the image?
#or, um, not the image... oh i see, i have 'photo' and i have 'image', 
for x in range(0, 520, 5):
  loadpic(crsr, conn, x)

