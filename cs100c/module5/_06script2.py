#embedded sql scripts including show database & add data

#notes:
#it doesn't like comparing None
#list was the key to displaying a list of databases
#i ended up using regular expressions when database items were hard to strip
#use join correctly (it's not the same as append); it helps to use tuples
#correct datatypes also help

#it always puts a b before the value for the last column. wat is this???

#well, i'm having problems with:
#create new column > a. exits the program, when i try to return to COLUMN MENU!
#create new column > b. gets stuck on types[d]????

def show_db():

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
        base = 'null_name'
        while base not in dblist:
            base = input('enter the name of a database to insert data: ')

    show.close()

    return base

def show_tables():

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
        tabel = 'null_name'
        while tabel not in tblist:
            tabel = input('enter the name of a table to insert data: ')

    tables.close()

    return tabel


def show_columns(tabel):
    
    describen = "select * from " + tabel
    rows = sdb.cursor()
    rows.execute(describen)
    row_count = rows.rowcount
    columns = [name for (name, _, _, _, _, _, _) in rows.description]

    for row in rows:
        rowlist = list(row)
        print(rowlist)

    rows.close

    return columns, row_count, rowlist

def create_insert(rowlist):
    base1 = "insert into " + tabel + " (`"
    base2 = "`) values ('"
    base3 = "')"

    print('Enter a value for each of these columns, or None for no value: ')
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
    print('new row created.')

def select_type(types, inuse, length):
    dt = 0
    while dt == 0:

        print(f'SELECT DATA TYPE\ncurrent datatype is{types[inuse]}(0).')

        select = 'null_name'
        while select != 'm' and select not in types:
            print('available datatypes:')
            for d in types:
                print(f'{d}. {types[d]}')
        
        select = input('enter one of these datatypes: ')
        inuse = types.index(select)

        print(f'\nnew datatype & length: {types[inuse]}({length})')
        dt = input('press 0 to select length again, or 1 to return to COLUMN MENU: ')

    if dt == 1:
        column_menu()

    return inuse
    
def set_range(types, inuse, length, lens):
    rng = 0
    while rng == 0:

        print(f'\nSELECT LENGTH\ncurrent datatype is {types[inuse]}({length}).')

        length = -1
        while int(length) not in range(0, lens[inuse]):
            print(f'available length: 0, {lens[inuse]}')
            length = input('set range max: ')

        print(f'\nnew datatype & length: {types[inuse]}({length})')
        rng = input('press 0 to select length again, or 1 to return to COLUMN MENU: ')

    if rng == 1:
        column_menu()

    return length

def column_menu():
    length = -1
    types = ['varchar', 'int', 'char', 'bool']
    lens = [65535, 255, 255, 1]
    inuse = 0

    print(f'\nCOLUMN MAIN MENU\ncurrent datatype is {types[inuse]}({length}).')
    lentype = 'null_name'
    while lentype != 'a' and lentype != 'b' and lentype != 'c':
        lentype = input('press a to select a different length.\npress b to select a different datatype.\npress c to create column. ')


    if lentype == 'a':
        
        length = set_range(types, inuse, length, lens)

    elif lentype == 'b':

        inuse = select_type(types, inuse, length)

    elif lentype == 'c':

        if length < 0:
            print('\nyou need to set length first.')
            column_menu()
        else:
            column_name(tabel, inuse, length, lens)


def column_name(tabel, inuse, length, lens):

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

    if nm == 1:
        execute_column(tabel, inuse, length, lens, cname)


def execute_column(tabel, inuse, length, lens, cname):

    newc = f'alter table {tabel} add {cname} {lens[inuse]}({length})'
    newcex = sdb.cursor()
    newcex.execute(newc)
    print(f'inserting column {cname} {inuse}({length}) into {tabel}')


    newcex.close()



import pymysql
import re

db = pymysql.connect(host='localhost', user='root', password = '2101')
db.autocommit(True)

#enter the name of a database to insert data
base = show_db()

db.close()


#reconnected at new database?        
sdb = pymysql.connect(host='localhost', user='root', password = '2101', database = base)
sdb.autocommit(True)


input('now in database ' + base + '. press any key to show tables in ' + base + '.')
tabel = show_tables()

input('press any key to see existing columns in ' + tabel)
columns, row_count, rowlist = show_columns(tabel)


#do you want to a. create new row, or b. create new column?
c = 'null_name'
while c.lower() != 'a' and c.lower() != 'b':
    c = input('\ndo you want to a. create new row, or b. create new column? ')

if c == 'a':
    create_insert(rowlist)

elif c == 'b':
    column_menu()

sdb.close()




