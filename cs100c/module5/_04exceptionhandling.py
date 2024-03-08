#here are some sql error codes that look like they would be easy to replicate
#invalid character, nonexistent column/table, like predicate on nonstring 
#non-db errors... these are harder to think of! 
#oh, haha, well here's one right here, object of type set is not JSON serializable (i wrote the squiggly part wrong)

#i forgot that get_employees was the one i stored, so i was trying to display all procedures, didn't really work
"""
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
"""
#well, i took away the outer shell, and i still need to figure it out
#it seems to not like my __getattribute__???

#i tried with the whole thing, with fixed exception, but it's still complaining about tuples! selected * and 'tuple' object has no attribute 'ID'?
#so like... what, am i not indexing something correctly? also, where is ID coming from???
#oh ok, so id is the first... thing?
#ok, so what are we trying to do here anyway? with the weird columns part? like, is that just formatting?

#uhhh, the first way i think to do this is a count, which is like, awkward, i know, but what is that __getattribute__???

import pymysql

db = None
crsr = None
success = False
while not success:
    try:
        db = pymysql.connect(host='localhost', user='root', password='2101', database = 'northwind')
        db.autocommit(True)
        crsr = db.cursor()
        while not success:
            sql = input('type an SQL string: ')
            try:
                res = crsr.execute(sql)
                #ignore these columns in crsr.description:
                #type_code, display_size, internal_size, precision, scale, null_ok
                columns = [name for (name,__,__,__,__,__,__) in crsr.description]
                for row in crsr:
                    count = 0
                    for col in columns:
                        print(f'{col}: {row[count]}')
                        count += 1
                    print()
                    success = True      
            except pymysql.Error as dberror:
                (errcode, errmsg) = dberror.args
                print(errmsg)
                print("Let's try again...")
    except Exception as err:
        print('some non-db error occurred: ' + str(err))
        success = True

if crsr is not None:
    crsr.close()
if db is not None:
    db.close()
