#alas! i can't always initialize with None, because it doesn't like comparing None! is this true? because i'm having other comparison issues
#i got around the latest with a null name, although that doesn't seem entirely legit
#oh, never mind, i don't know if i'll need that anyway, because i'm not sure how to get around this without a duplicate loop
#aha! the solution was a list!
#why am i having trouble stripping??? i ended up using regular expressions

import pymysql
import re

db = pymysql.connect(host='localhost', user='root', password = '2101')
db.autocommit(True)

showdb = "show databases;"
show = db.cursor()
x = input('press any key to show existing databases.')
show.execute(showdb)
row_count = show.rowcount
dblist = []
for row in show:
    print(row)
    dblist.append(re.sub('[^\w]', '', str(row)))
if row_count == 0:
    print(f'No databases found.')

n = 'null_name'
while n not in dblist:
    n = input('enter the name of a database to insert data: ')

        
sdb = pymysql.connect(host='localhost', user='root', password = '2101', database = n)
sdb.autocommit(True)

p = input('now in database ' + n + '. press any key to show tables in ' + n + '.')

sql = input('insert into ' + n)



show.close()