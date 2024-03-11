#embedded sql scripts including show database & add data

#notes:
#it doesn't like comparing None
#list was the key to displaying a list of databases
#i ended up using regular expressions when database items were hard to strip
#use join correctly (it's not the same as append); it helps to use tuples
#correct datatypes also help

#it always puts a b before the value for the last column. wat is this???

#anyway... type selection is going to take forever!!! i don't have time for this right now!!!

import pymysql
import re

def get_length(max):
    length = print(f'enter a number between 0 and {max}: ')
    return length

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
    
    stringtuple = (base1, base2, base3)
    string = "".join(stringtuple)
    str = sdb.cursor()
    str.execute(string)


elif c == 'b':

    vartuples = [('varchar', 65535),('int',255),('char',255),('datetime',0),('bool', 1)]

    s = 'null_name'
    while s != 'a' and s != 'b':
        print('COLUMN DATATYPE\n default datatype is varchar.\n')
        print('press a to select a length for your varchar.\npress b to select a different datatype for your column')

        if s == 'b':
            while sb != 'm' and sb != 'int' and sb != 'char' and sb != 'datetime' and sb != 'bool':
                print('available datatypes:\n 1.int, 2.char, 3.datetime, 4.bool')
                sb = input('enter one of these datatypes, or press m to return to the COLUMN DATATYPE menu')

    newt = f'alter table {n} add {cname} {}
    newc = sdb.cursor()

newc.close()
sdb.close()
tables.close()
rows.close()




