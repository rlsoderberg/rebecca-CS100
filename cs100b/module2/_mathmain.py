from student import Student
from quizquestion import QuizQuestion

import random

def main():
    #create quiz question object
    #i had to initialize the lists with a value inside, otherwise it complained about list[-1]
    xlist = [0]
    ylist = [0]
    symblist = ['']
    q = QuizQuestion(xlist, ylist, symblist)

    #create student object
    stud = Student('roberta', 24223, '7/4/1982', 5)

    #get name from student class
    name = stud.name

    #initialize totalcorrect
    totalcorrect = 0

    #open file to write . make sure to get correct filename
    file = open('_equations.txt', 'w')

    #loop to generate 10 random math equations
    for loopcount in range(0, 10):
        print(f'\nproblem {(loopcount + 1)}')
        #initially set repeat to 0 (no repeat)
        repeat = 0
        newcorrect = 0

        #choose operation symbol outside, so it stays the same
        oplist = ['+', '-', '*']
        opnum = random.randrange(0, 3) 

        #example of doing stuff with gradelevel
        if stud.gradelevel < 5:
            max = 6
        else:
            max = 20
        
        #generate random x & y
        x = random.randrange(1, max)
        y = random.randrange(1, max)
        #duplicate forbidder. well... i'm not entirely sure if this is working...
        while x == q.xlist[-1] and y == q.ylist[-1]:
            x = random.randrange(1, max)
            y = random.randrange(1, max)
        
        #while loop for problem
        while newcorrect == 0:
            #get/reuse symbol
            if repeat == 1:
                symb = q.symblist[-1]
            elif repeat == 0:
                symb = oplist[opnum]
                q.symblist.append(symb) 

            #execute equation, first getting computer answer
            eqtuple = q.get_compans(repeat, x, y)
            #unpack eqtuple, which contains computer answer & repeat
            (compans, repeat) = eqtuple

            #write equation to file
            file.write(str(x) + " " + str(symb) + " " + str(y) + " = " + str(compans) + "\n") 
            #get userans from problem interaction
            newcorrect = q.get_userans(loopcount, x, y, compans)

            #ah, this is how we deal with repeat/newcorrect! nice and simple!
            if repeat == 0:
                totalcorrect = totalcorrect + newcorrect
            repeat = 1

    #close file
    file.close()

    #print overall results
    print(f'\n{name} answered {totalcorrect} out of 10 questions correctly.\n')
        
main()

        
        


