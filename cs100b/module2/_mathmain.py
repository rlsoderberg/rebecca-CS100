from student import Student
from quizquestion import QuizQuestion

def main():
    #create quiz question object
    q = QuizQuestion()

    #ask user for their name
    name = input('please enter your name: ')

    #initialize correct
    correct = 0

    #open file to write . make sure to get correct filename
    file = open('_equations.txt', 'w')

    #loop to generate 10 random math equations
    for loopcount in range(0, 10):
        repeat = 0
        eqtuple = q.probloop(loopcount, repeat, file)
        #unpack eqtuple
        (compans, userans, repeat) = eqtuple
        if repeat == 0:
            newcorrect = 1
        elif repeat == 1:
            newcorrect = 0
            while repeat == 1:
                repeat = q.probloop(loopcount, repeat, file)
        correct = correct + newcorrect
        #oh, you just put this in here, and then you don't need all that bonky enumerate stuff
        print(f'Correct Answer: {compans} -- User Answer: {userans}\n')

    #close file
    file.close()

    #print overall results
    print(f'\n{name} answered {correct} out of 10 questions correctly.\n')
        
main()

        
        


