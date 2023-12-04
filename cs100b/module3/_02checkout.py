import collections
import random

#so, last time i did this problem, i had the problem of people joining the line and immediately leaving
#i somehow solved it, so let me try and copy. putting line events in functions might help
#well, i think the problem is, for tired of waiting, i now have popleft, and these people have no patience

#person class contains name
class Person():
    def __init__(self, name = 'Bob'):
        self.name = name

#create person object & add to end of line
def addperson():
    #pick random name, using our nifty choice function (collections is a module, choice is a function)
    randomname = random.choice(names)
    #create person object
    person = Person(randomname)
    #line is going left to right
    line.appendleft(person)
    #explain what is happening
    print(f'{person.name} joined the line')

def linerand():
    #random choice of line events
    randomnum = random.randrange(0, 3)
    if randomnum == 0:
        #serve front person
        person = line.pop()
        print(f'now serving {person.name}')
    else:
        addperson()

def removeperson():
    #remove person from end of line
    person = line.popleft()
    print(f'{person.name} is tired of waiting')

#read names from file
f = open('people.txt', 'r')
#read always feels kind of weird to me, like last time i tried readline, but i like this better
#split by line & turn into a list
names = f.read().split('\n')
f.close()

#create line deque
line = collections.deque()

#for loop for line events
for x in range(0, 100):
    
    #in this case, if/elif/else help to keep things in order
    if len(line) < 3:
        addperson()

    elif len(line) > 6:
        removeperson()

    else:
        linerand()




    

