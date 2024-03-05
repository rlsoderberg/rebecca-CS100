#we are back to python files!!! nice green comments

#i totally stole this row counter off the internet!!! it looks pretty nice though

#the one with the languages isn't working!!! 
#there should totally be some results for french!!!
#i think i'm formatting it wrong...

#discounts is also not working
#it's giving me all these discounts of 0!!!

import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = '2101', database = 'northwind')
db.autocommit(True)

#lname = input('give me a last name to search for: ')
#lang = input('you are looking for employees with experience in what language? ')
#disc = input('find products with discount over: ')

#sql = "select `first name`, `last name` from employees where `last name` = '"+lname+"'"
#sql = "select `first name`, `last name`, notes from employees where notes like '"%lang%"' "
#sql = "select p.`product name`, od.discount from products p join `order details` od on p.id = od.`product id` where discount >= 'disc'"

crsr = db.cursor()
res = crsr.execute(sql)

row_count = crsr.rowcount
for row in crsr:
    #print(row[0] + ' ' + row[1])
    #print(row[0] + ' ' + row[1] + ': ' + row[2])
    #print(row[0] + ': discount of ' + str(row[1]))
if row_count == 0:
    #print(f'No employees with last name {lname}.')
    #print(f'No employees with {lang} experience.')
    #print(f'No products with discount over {disc}.')
crsr.close()
db.close()