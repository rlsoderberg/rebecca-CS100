#embedded sql with pymysql
#access database, execute sql command, go through result row by row

#there are 3 different lines for the input/sql statement/print result/print failure parts of the code, for 3 different versions of the problem

import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = '2101', database = 'northwind')
db.autocommit(True)

#lname = input('give me a last name to search for: ')
#lang = input('you are looking for employees with experience in what language? ')
valid = False
while valid == False:
    try:
        input = int(input('enter product id to see the ids of orders containing that product: '))
        valid = True
    except ValueError:
        print('please enter a valid integer: ')

prod = str(input)


#sql = "select `first name`, `last name` from employees where `last name` = '" + lname + "'"
#sql = "select `first name`, `last name`, notes from employees where notes like '%" + lang + "%'"
sql = "select p.id, p.`product name`, od.`order id` from products p join `order details` od on od.`product id` = p.id where p.id = '" + prod + "'"

crsr = db.cursor()
res = crsr.execute(sql)

row_count = crsr.rowcount
for row in crsr:
    #print(row[0] + ' ' + row[1])
    #print(row[0] + ' ' + row[1] + ': ' + row[2])
    print('id: ' + str(row[0]) + ' product name: ' + str(row[1]) + ' order id: ' + str(row[2]))
if row_count == 0:
    #print(f'No employees with last name {lname}.')
    #print(f'No employees with {lang} experience.')
    print(f'No products found with id {prod}.')
crsr.close()
db.close()