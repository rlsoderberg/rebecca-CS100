import collections
import random

import sys

class Person:
    def __init__(self, name):
        self.name = name

#sys.path.append('../../cs100a/module4')
line = collections.deque()
names = open("../../cs100a/module4/names.txt", "r").read().split("\n")

def addperson():
    name = names[random.randrange(0, len(names))]
    print(name+" joined the line")
    person = Person(name)
    line.appendleft(person)

#where is the 100 going???
for i in range(0, 100):
    if len(line) < 3:
        addperson()
    if len(line) >= 3 and len(line) <= 6:
        randome = random.randrange(0, 2)
        if randome == 0:
            front = line.pop()
            print("now serving "+front.name)
        elif randome == 1 or randome == 2:
            addperson()
    if len(line) > 6:
        back = line.popleft()
        print(back.name+" is tired of waiting")

