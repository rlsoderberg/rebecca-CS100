import collections
import random

import sys
sys.path.append('../..')

from i import maine

class Person:
    def __init__(self, name):
        self.name = name

line = collections.deque()
names = open("names.txt", "r").read().split("\n")

def addperson():
    name = names[random.randrange(0, len(names))]
    print(name+" joined the line")
    person = Person(name)
    line.appendleft(person)

#where is the 100 going???
for i in (0, 100):
    while len(line) < 3:
        addperson()
    while 3 <= len(line) <= 6:
        randome = random.randrange(0, 2)
        if randome == 0:
            front = line.pop()
            print("now serving "+front.name)
        elif randome == 1 or randome == 2:
            addperson()
    while len(line) > 6:
            back = line.popleft()
            print(back.name+" is tired of waiting")

