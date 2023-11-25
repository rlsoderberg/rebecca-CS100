#import random for math
import random

#ask user for their name
name = input('please enter your name: ')

#initialize correct count and loop count
correctcount = 0

#loop to generate 10 random math equations
for loopcount in range(0, 10):

    #choose operation
    oplist = ['+', '-', '*', '/', '%']
    #oh cool, you could use lambda to choose operations!
    #now, i don't REALLY know how to do this, i just stole this from some person on the internet
    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y
          }
    opnum = random.randrange(0, 3)
    symb = oplist[opnum]
    
    #choose variables
    x = random.randrange(1, 6)
    y = random.randrange(1, 6)

    #solve equation
    compans = op[str(symb)](x,y)

    #print equation, get user input
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
        correctcount += 1
    elif userans != compans:
        print(f'user answer({userans}) is incorrect. correct answer is {compans}.')

#print overall results
print(f'\nuser answered {correctcount} out of 10 questions correctly.\n')


    
    


