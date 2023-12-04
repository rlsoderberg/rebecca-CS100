import collections
import random

from student import Student

def main():
    #this is how you create a dictionary!!! curly brackets = {}
    #because... square brackets are used by list, indexing... parentheses are used by tuples, paramaters... 
    roster = {}
    names = ['alice', 'bob', 'carol', 'dave', 'edith', 'fred']
    #hey, i was going to try sticking these in there too, more or less, but idk
    #so it gives me an error when it gets to item 6, i think. not sure how to get around that
    birthdates = ['5/5/1955', '6/6/1966', '7/7/1977', '8/8/1988', '9/9/1999', 'N/A']

    #is range a way to get around the whole weird python intuitive for loop thing?
    for n in range (0, len(names)):
        #create student with random id
        id = random.randrange(1, 100000)
        roster[id] = Student(id, names[n], birthdates[n])
    
    #show ids in roster
    print('here are the student ids in your roster: ')
    for s in roster:
        print(s)

    #initialize id
    id = 0

    #show name corresponding to selected id
    i = input("which id would you like information on? type -1 to quit ")
    i = int(i)
    #oh, what's this? a dictionary is directly searchable? niiice
    #wait, how does this work? i thought the roster was the thing indexed by id
    #meaning, its actual contents are the names?
    #so, ok, so the dictionary is indexed by id
    #but dictionary items are ALSO equal to an object, so you can access... a lot of other properties?
    
    #well, i'm going to try putting this in... a try except???
    i = 0
    while i != -1:
        i = input("which id would you like information on? type -1 to quit ")
        i = int(i)
        valid = False
        while valid == False:
            try:
                if i in roster:
                    print(f'{str(i)}: {roster[i].name}. birthdate: {roster[i].birthdate}')
                valid = True
            except i not in roster:
                print(f'{str(i)}: {roster[i].name}. birthdate: {roster[i].birthdate}')
            
    #well... at least it quits
    print('goodbye')

main()