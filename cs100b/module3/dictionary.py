import random

import sys
sys.path.append('../..')

from i import maine

type = "int"
antiblanky = 1

class Student:
    def __init__(self, id=0, name=""):
        self.id = id
        self.name = name

roster = {}
names = ['amaryllis', 'betelgeuse', 'clematis', 'demeter', 'echinacea', 'facula']
for n in names:
    id = random.randrange(10000, 99999)
    roster[id] = Student(id, n)

print('here are the students in roster')
for s in roster:
    print(s)

print('which id would you like information on? type -1 to quit: ')
i = maine(type, antiblanky)
i = int(i)
while i != -1:
    if i in roster:
        print(str(i)+" : "+roster[i].name)
    else:
        print('student not found')
    i = input('which id would you like information on? type -1 to quit: ')
    i = int(i)