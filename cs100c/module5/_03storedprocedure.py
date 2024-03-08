#this example isn't even working for me, like what even is that? with the delimiters and stuff???
#i tried:
#create procedure get_employees begin declare @lname varchar(255); select `last name`, `first name` from employees where `last name` = @lname; end;
#hey, i didn't get any errors on that one...

import pymysql

db = pymysql.connect(host='localhost', user='root', password='2101', database='northwind')
db.autocommit(True)
lname = input('give me a last name to search for: ')
sql = "call get_employees(%s)"
crsr = db.cursor()
res = crsr.execute(sql, [lname])
for row in crsr:
    print(row[0] + ' ' + row[1])

crsr.close()
db.close()

#well, i ended up with error 'procedure get_employees does not exist', so i'm pretty sure that didn't work...
#oh, hahaha, i see why i got no errors with my create procedure, i forgot to take out the hashtag at the beginning

#well, i guess the example is supposed to be used with workbench
#oh good lord! now i have to figure out where my northwind file is, and figure out how to access it with workbench!
#oh right, i guess i just pasted it in
#ok, it seemed to work when i went up to database and said connect to database
#ooh!!! it worked!!!

#so that was...
"""
use northwind;
delimiter \\

CREATE PROCEDURE `get_employees` (
	in lname varchar(255)
)
BEGIN
	select `last name`, `first name`
    from employees
    where `last name` = lname;
END \\

delimiter ;
"""

# i never exactly did the procedure storage part of this? you know, applying to additional example queries?
