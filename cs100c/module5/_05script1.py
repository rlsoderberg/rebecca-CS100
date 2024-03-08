#i created an extra cursor because idk how else to execute?
#it doesn't like when i try to create a database called databases!!! what's the deal?

import pymysql

db = pymysql.connect(host='localhost', user='root', password = '2101')
db.autocommit(True)
name = input('what will you name your database? ')
sql = "create database " + name + ";"
print(sql)
showdb = "show databases;"
create = db.cursor()
cr = create.execute(sql)
create.close()

show = db.cursor()
x = input('press any key to show existing databases.')
show.execute(showdb)
row_count = show.rowcount
for row in show:
    print(row)
if row_count == 0:
    print(f'No databases found.')
show.close()

db.close()

