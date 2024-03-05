#we are back to python files!!! nice green comments

#i totally stole this row counter off the internet!!! it looks pretty nice though

#the one with the languages isn't working!!! 
#there should totally be some results for french!!!
#i think i'm formatting it wrong...
#aha, i had to put the percent signs outside the first set of quotes

#discounts is also not working
#it's giving me all these discounts of 0!!!
#hey, are all the discounts 0?
#ok, i'm using profit margin

#well, the inequality still isn't working
#i converted input to int, but that didn't seem to help
#seems as if maybe my problem might be with min on line 29??? not sure
#i tried to convert everything to floats, and now it's just not working
#well, i decided to try to stick with ints, since that's the datatype of my generated column
#how silly! i don't know what i'm doing!
#i'm whipping out the old try except...

#well, i tried to change it to get exact profit margin, and now it's acting even weirder!
#you know, i wouldn't be surprised if the generated column was messing with it, so maybe i'll try a different column later

import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = '2101', database = 'northwind')
db.autocommit(True)

#lname = input('give me a last name to search for: ')
#lang = input('you are looking for employees with experience in what language? ')
valid = False
while valid == False:
    try:
        min = int(input('find products with profit margin of: '))
        valid = True
    except ValueError:
        print('please enter an integer.')



#sql = "select `first name`, `last name` from employees where `last name` = '"+lname+"'"
#sql = "select `first name`, `last name`, notes from employees where notes like '%"+lang+"%' "
#sql = "select `product name`, `profit margin` from products p where `profit margin` > 'min'"
sql = "select `product name`, `profit margin` from products p where `profit margin` = 'min'"

crsr = db.cursor()
res = crsr.execute(sql)

row_count = crsr.rowcount
for row in crsr:
    #print(row[0] + ' ' + row[1])
    #print(row[0] + ' ' + row[1] + ': ' + row[2])
    #print(row[0] + ': profit margin of ' + str(row[1]))
    print(row[0] + ': profit margin of ' + str(row[1]))
if row_count == 0:
    #print(f'No employees with last name {lname}.')
    #print(f'No employees with {lang} experience.')
    print(f'No products with discount of {min}.')
crsr.close()
db.close()