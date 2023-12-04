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

    #OH!!! i spent forever trying to figure out why i had an extra query, when IT WAS UP HERE THE WHOLE TIME!!!
    i = input("which id would you like information on? type -1 to quit ")
    
    complete = 0
    while i != -1:
        #show question again on further loops
        if complete == 1:
            i = input("which id would you like information on? type -1 to quit ")
        if int(i) in roster:
                print(f'{str(i)}: {roster[int(i)].name}. birthdate: {roster[int(i)].birthdate}')
        complete = 1
            
    print('goodbye')
    
main()