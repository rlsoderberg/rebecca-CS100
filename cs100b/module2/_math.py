from student import Student
from quizquestion import QuizQuestion

#import random for math
import random

#define equation for contents of problem loop
def probloop(loopcount, repeat, file):
    #declaring global variables inside function lets us change them from within
    global x
    global y
    
    if repeat == 0:
        #generate random operation symbol
        #list of operation symbols
        #i tried putting randop in its own function 
        #it was pretty much the only part of this problem lump that i knew how to separate out
        oplist = ['+', '-', '*']
        opnum = random.randrange(0, 3)
        symb = oplist[opnum]
        symblist.append(symb)
    if repeat == 1:
        symb = symblist[-1]

    #oh cool, you could use lambda to choose operations!
    #now, i don't REALLY know how to do this, i just stole this from some person on the internet
    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y
          }

    #depending on whether you've run the loop before, generate & store x & y, or take from list
    if repeat == 0:
        #trying to prevent repeat problems. hard to tell if this is working!
        #oh wait, all we have to do is use xlist and ylist!
        while x == xlist[-1] and y == ylist[-1]:
            x = random.randrange(1, 6)
            y = random.randrange(1, 6)
        xlist.append(x)
        ylist.append(y)
    if repeat == 1:
        x = xlist[-1]
        y = ylist[-1]

    #solve equation
    compans = op[str(symb)](x,y)


    #i am writing these to a file. make sure to use newline
    file.write(str(x) + " " + str(symb) + " " + str(y) + " = " + str(compans) + "\n") 

    #print equation
    valid = False
    while valid == False:
        try:
            userans = int(input(f'\n{(loopcount + 1)}. {x} {symb} {y} = '))
            if userans == '':
                raise ValueError('empty input')
            valid = True
        except ValueError:
            print('invalid input')

    #display results; modify correct count
    if userans == compans:
        print(f'user answer({userans}) is correct.')
        repeat = 0
    elif userans != compans:
        print(f'user answer({userans}) is incorrect. try again!')
        repeat = 1

    #write equation tuple (equation, correct answer, user answer) to equation list
    eq = (str(x) + " " + str(symb) + " " + str(y))
    #oh right, so is double parentheses kind of like, a shortcut for these two lines?
    eqtuple = (eq, compans, userans, repeat)
    
    #if i'm separating probloop into another file, i'm pretty sure i want to return eqtuple, insted of repeat
    #or, i guess i could put repeat IN the tuple
    return eqtuple

#this belongs somewhere, not sure where yet
equationlist.append(eqtuple)

def resultloop(index, tuple):
    (eq, compans, userans, repeat) = tuple
    print(f'{index}. {eq}\nCorrect Answer: {compans} -- User Answer: {userans}\n')

#lists where we store x, y, and symb
xlist = [0]
ylist = [0]
symblist = ['']
equationlist = []

#initialize x and y
#they are global variables!
x = 0
y = 0


#define main
def main():
    #ask user for their name
    name = input('please enter your name: ')

    #initialize correct
    correct = 0

    #open file to write . make sure to get correct filename
    file = open('04equations.txt', 'w')

    #loop to generate 10 random math equations
    for loopcount in range(0, 10):
        repeat = 0
        repeat = probloop(loopcount, repeat, file)
        if repeat == 0:
            newcorrect = 1
        elif repeat == 1:
            newcorrect = 0
            while repeat == 1:
                repeat = probloop(loopcount, repeat)
        correct = correct + newcorrect

    #close file
    file.close()

    #print overall results
    print(f'\n{name} answered {correct} out of 10 questions correctly.\n')

    #print results, with equation, correct answer, and user answer
    for index, tuple in enumerate(equationlist, start = 1):
        #right, so i'm using x to represent a particular tuple in equationlist...
        #but how do i get a numerical value for x? enumerate?
        resultloop(index, tuple)


main()

    
    


