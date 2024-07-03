import collections 
import random

#person object contains name
class Person():
    def __init__(self, name):
        self.name = name

#read names from file, split by line
f = open("people.txt", "r")
#create names list on a separate line, so you can close the file...
names = f.read().split("\n")
#create deque for people in line
line = collections.deque()

#function adds person, both if line < 3, and if r != 0
def add_person():
    #random name
    name = names[random.randrange(0, len(names))]
    n = Person(name)
    #line moves rightward
    line.appendleft(n)
    print(f'{n.name} joined the line')

#line_rand executes a random action if line is of a moderate length
def line_rand():
    r = random.randrange(0, 3)
    if r == 0:
        s = line.pop()
        print(f'now serving {s.name}')
    else:
        n = add_person()
    
#main chooses something to happen to the line, depending on how big the line is
def main():
    for x in range(0, 100):
        if len(line) < 3:
            add_person()
        elif len(line) > 6:
            w = line.pop()
            print(f'{w.name} is tired of waiting')
        else: line_rand()

main()

#close file
f.close()

