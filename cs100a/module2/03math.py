#import random for math
import random

#ask user for their name
name = input('please enter your name: ')

#initialize correct
correct = 0

#define function to pick random operation symbol
def randop():
    #list of operation symbols
    oplist = ['+', '-', '*', '/', '%']
    opnum = random.randrange(0, 3)
    symb = oplist[opnum]

    return symb

#define equation for contents of problem loop
def probloop(correct):
    #generate random operation symbol
    symb = randop()

    #oh cool, you could use lambda to choose operations!
    #now, i don't REALLY know how to do this, i just stole this from some person on the internet
    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y
          }


    #choose variables
    x = random.randrange(1, 6)
    y = random.randrange(1, 6)

    #solve equation
    compans = op[str(symb)](x,y)

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
        correct = 1
    elif userans != compans:
        print(f'user answer({userans}) is incorrect. correct answer is {compans}.')

    return correct

#loop to generate 10 random math equations
for loopcount in range(0, 10):
    newcorrect = probloop(correct)
    correct = correct + newcorrect


#print overall results
print(f'\n{name} answered {correct} out of 10 questions correctly.\n')


    
    


