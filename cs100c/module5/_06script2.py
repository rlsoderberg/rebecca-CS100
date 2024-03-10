#alas! i can't always initialize with None, because it doesn't like comparing None! is this true? because i'm having other comparison issues
#i got around the latest with a null name, although that doesn't seem entirely legit
#oh, never mind, i don't know if i'll need that anyway, because i'm not sure how to get around this without a duplicate loop
#aha! the solution was a list!
#why am i having trouble stripping??? i ended up using regular expressions

#anyway... is there some way i can just add a database onto my connection? instead of creating a whole new one?
#well, i tried the column thing from a previous problem, but it's totally still not working!
#i've got it where it really doesn't make sense... 

#well, i'm converting to list, and then printing whole rows. not pretty, but somewhat functional?
#it would be nice to make it look pretty, i kind of got stuck on python for loops, which always weird me out a little!!!
#i mean, obviously the fundamental problem is that i'm dealing with cursors and stuff, but i'm skipping that for now

#i haven't quite gotten to the point where i'm actually putting the row in the database...

#my first attempt at for loop insertion failed spectacularly
#i just tried another way and it didn't work at all! 
#i might be using join wrong...

#i had to make these tuples first
#now it says my values are incorrect!!!

#oh!!! maybe my datatypes are incorrect!!!
#there, i think that worked

#what a mess!!! i mean, first of all, selecting rows using the first column is super sketchy, can't expect that to be a primary key
#but i will try adding new columns later, that might work

import pymysql
import re

db = pymysql.connect(host='localhost', user='root', password = '2101')
db.autocommit(True)

x = input('press any key to show existing databases.')
showdb = "show databases;"
show = db.cursor()
show.execute(showdb)
row_count = show.rowcount
dblist = []
for row in show:
    print(row)
    dblist.append(re.sub('[^\w]', '', str(row)))

if row_count == 0:
    print(f'No databases found.')
else:
    n = 'null_name'
    while n not in dblist:
        n = input('enter the name of a database to insert data: ')
        
db.close()
show.close()

        
sdb = pymysql.connect(host='localhost', user='root', password = '2101', database = n)
sdb.autocommit(True)

p = input('now in database ' + n + '. press any key to show tables in ' + n + '.')
showtables = "show tables;"
tables = sdb.cursor()
tables.execute(showtables)
row_count = tables.rowcount
tblist = []
for row in tables:
    print(row)
    tblist.append(re.sub('[^\w]', '', str(row)))

if row_count == 0:
    print(f'No tables found.')
else:
    n = 'null_name'
    while n not in tblist:
        n = input('enter the name of a table to insert data: ')

f = input('press any key to see existing columns in ' + n)
describen = "select * from " + n
rows = sdb.cursor()
rows.execute(describen)
row_count = rows.rowcount
columns = [name for (name, _, _, _, _, _, _) in rows.description]

for row in rows:
    rowlist = list(row)
    print(rowlist)




c = 'null_name'
while c.lower() != 'a' and c.lower() != 'b':
    c = input('\ndo you want to a. create new row, or b. create new column? ')
if c == 'a':

    base1 = "insert into " + n + " (`"
    base2 = "`) values ('"
    base3 = "')"

    m = print('Enter a value for each of these columns, or None for no value: ')
    for e in range(0, len(rowlist)):
        
        item = input(columns[e] + ': ')
        tuple1 = (base1, columns[e])
        if e > 0:
            base1 = "`, `".join(tuple1)
        else: 
            base1 = "".join(tuple1)
        tuple2 = (base2, item)
        if e > 0:
            base2 = "', '".join(tuple2)
        else:
            base2 = "".join(tuple2)
    

sdb.close()
tables.close()
rows.close()




