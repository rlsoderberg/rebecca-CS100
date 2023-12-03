from student import Student
from quizquestion import QuizQuestion

import random

def main():
    #create quiz question object
    #i had to initialize the lists with a value inside, otherwise it complained about list[-1]
    xlist = [0]
    ylist = [0]
    symblist = ['']
    x = 0
    y = 0
    q = QuizQuestion(xlist, ylist, symblist, x, y)

    #ask user for their name
    name = input('please enter your name: ')

    #initialize totalcorrect
    totalcorrect = 0

    #open file to write . make sure to get correct filename
    file = open('_equations.txt', 'w')

    #loop to generate 10 random math equations
    for loopcount in range(0, 10):
        #initially set repeat to 0 (no repeat)
        repeat = 0
        #generate random x & y
        x = random.randrange(1, 6)
        y = random.randrange(1, 6)
        #execute equation, first getting computer answer
        eqtuple = q.get_compans(repeat, file, x, y)
        #unpack eqtuple, which contains computer answer, repeat, and symbol
        (compans, repeat, x, y) = eqtuple
        #get userans from problem interaction
        userans = q.get_userans(loopcount, x, y)
        #finally, display result
        repeat = q.display_result(userans, compans)

        if repeat == 0:
            newcorrect = 1
        elif repeat == 1:
            newcorrect = 0
            while repeat == 1:
                eqtuple = q.get_compans(repeat, file, x, y)
        totalcorrect = totalcorrect + newcorrect

    #close file
    file.close()

    #print overall results
    print(f'\n{name} answered {totalcorrect} out of 10 questions correctly.\n')
        
main()

        
        


