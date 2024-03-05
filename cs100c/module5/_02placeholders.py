#sanitizing input by using %s as a placeholder
#add lname as list, using brackets

#lname = 'Kotas'; drop table employees; --'; employees still exists
#i don't get exactly how that worked?
#i also don't get why there's a comment at the end?>


import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = '2101', database = 'northwind')
db.autocommit(True)

lname = input('give me a last name to search for: ')
sql = "select `first name`, `last name` from employees where `last name` = %s"

crsr = db.cursor()
res = crsr.execute(sql, [lname])

for row in crsr:
    print(row[0] + ' ' + row[1])

crsr.close()
db.close()