#here are some sql error codes that look like they would be easy to replicate
#invalid character, nonexistent column/table, like predicate on nonstring 
#non-db errors... these are harder to think of! 
#oh, haha, well here's one right here, object of type set is not JSON serializable (i wrote the squiggly part wrong)

#i forgot that get_employees was the one i stored, so i was trying to display all procedures, didn't really work

import pymysql
import json


"""
db = None
crsr = None
try:
    db = pymysql.connect(host='localhost', user='root', password='2101', database='northwind')
    db.autocommit(True)
    name = input('give me a name to search for: ')
    sql = "call get_employees(%s)"
    print(sql)
    crsr = db.cursor()
    res = crsr.execute(sql, [name])
    ret = []
    for row in crsr:
        ret.append({'first name':row[0], 'last name':row[1]})
        print(json.dumps(ret))
except pymysql.Error as dberror:
    (errcode, errmsg) = dberror.args
    print(errmsg)
except Exception as err:
    print('some non-db error occurred: ' + str(err))

print('almost done')
crsr.close()
db.close()
"""
#well, i took away the outer shell, and i still need to figure it out
#it seems to not like my __getattribute__???

db = None
crsr = None
success = False
while not success:
    try:
        db = pymysql.connect(host='localhost', user='root', password='2101', database='northwind')
        db.autocommit(True)
        crsr = db.cursor()
        sql = input('type an SQL string: ')
        res = crsr.execute(sql)
        # get the column names. We're ignoring the other parts: name
        #    type_code, display_size, internal_size, precision, scale, null_ok
        columns = [name for (name, _, _, _, _, _, _) in crsr.description]
        for row in crsr:
            for col in columns:
                print(row.__getattribute__(col), end=' ')
            print()
        success = True
    except pymysql.Error as dberror:
        (errcode, errmsg) = dberror.args
        print(errmsg)
        print("Let's try again ...")

if crsr is not None:
    crsr.close()
if db is not None:
    db.close()

    

