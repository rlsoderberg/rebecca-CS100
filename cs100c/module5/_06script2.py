#embedded sql scripts including show database & add data

#notes:
#it doesn't like comparing None
#list was the key to displaying a list of databases
#i ended up using regular expressions when database items were hard to strip
#use join correctly (it's not the same as append); it helps to use tuples
#correct datatypes also help

#it always puts a b before the value for the last column. wat is this???

#anyway... type selection is going to take forever!!! i don't have time for this right now!!!

#oh, list of tuples is ridiculous. ok, i will just make multiple lists. it seems less correct but whatever!!!
#ooh, when you have a list of strings, make sure it's not just one long string

#i don't think types[available] is what i'm getting after at all, but how do you do that???

#i'm omitting datetime because that's, like, a whole thing!

#and do i really need to be making so many cursors???

#ok, i obviously need to reorganize this whole thing, so the menus work right, but i'll give it a save


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
    strex = sdb.cursor()
    strex.execute(string)


elif c == 'b':

    contdt = 0
    while contdt == 0:
        length = -1
        types = ['varchar', 'int', 'char', 'bool']
        lens = [65535, 255, 255, 1]
        inuse = 0

        print(f'\nCOLUMN MAIN MENU\ncurrent datatype is {types[inuse]}({length}).')
        lentype = 'null_name'
        while lentype != 'a' and lentype != 'b':
            lentype = input('press a to select a different length.\npress b to select a different datatype. ')

        if lentype == 'b':

            dt = 0
            while dt ==0:

                print(f'SELECT DATA TYPE\ncurrent datatype is{types[inuse]}(0).')

                select = 'null_name'
                while select != 'm' and select not in types:
                    print('available datatypes:')
                    for d in types:
                        print(f'{d}. {types[d]}')
                
                select = input('enter one of these datatypes, or press m to return to the SELECT COLUMN DATATYPE menu: ')
                if select != 'm':
                    inuse = types.index(select)


        elif lentype == 'a':
            
            rng = 0
            while rng == 0:

                print(f'\nSELECT RANGE\ncurrent datatype is {types[inuse]}({length}).')

                length = -1
                while int(length) not in range(0, lens[inuse]):
                    print(f'available range: 0, {lens[inuse]}')
                    length = input('set range max: ')

                print(f'\nnew datatype & length: {types[inuse]}({length})')
                rng = input('press 1 to return to COLUMN MAIN MENU, or 0 to return to SELECT RANGE menu: ')

    nm = 0
    while nm == 0:

        print('SELECT COLUMN NAME')

        valid = False
        while valid == False:
            try:
                cname = input('type name for column, up to 128 characters: ')
                valid = True
            except len(cname) > 128:
                print('Error: column name length exceeds 128 characters. Try again: ')

        nm = input('press 1 to create column, or 0 to SELECT COLUMN NAME again')

        newc = f'alter table {n} add {cname} {lens[inuse]}({length})'
        newcex = sdb.cursor()
        newcex.execute(newc)
        print(f'inserting column {cname} {inuse}({length}) into {n}')


newcex.close()
strex.close()
sdb.close()
tables.close()
rows.close()




