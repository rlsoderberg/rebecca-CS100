#here are some sql error codes that look like they would be easy to replicate
#invalid character, nonexistent column/table, like predicate on nonstring 
#non-db errors... these are harder to think of! 
#oh, haha, well here's one right here, object of type set is not JSON serializable (i wrote the squiggly part wrong)

#i forgot that get_employees was the one i stored, so i was trying to display all procedures, didn't really work

import pymysql
import json


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

    

