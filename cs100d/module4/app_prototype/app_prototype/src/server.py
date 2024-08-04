# Module Imports
import mariadb
import sys
from read_data import lines


# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="2101",
        host="192.0.2.1",
        port=3306,
        database="images"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

def loadpic(x, lines):
    #assign variables to different lines of data file (is there an easy way to do this better?)
    #make sure to have the right number of things!!!
    line0 = lines[x]
    line1 = lines[x+1]
    line2 = lines[x+2]
    line3 = lines[x+3]
    line4 = lines[x+4]

    linelist = (line0, line1, line2, line3, line4)
    return linelist

# Get Cursor
cur = conn.cursor()

#insert values while looping
for x in range(0, len(lines), 5):
    linelist = loadpic(x, lines)
    (line0, line1, line2, line3, line4) = linelist
    cur.execute(
        "INSERT INTO employees (filename, decade, source, info, title) VALUES (%s, %s, %s, %s, %s)", 
        (line0, line1, line2, line3, line4))