#import random for math
import random

#define function to pick random operation symbol
def randop():
    #list of operation symbols
    oplist = ['+', '-', '*', '/', '%']
    opnum = random.randrange(0, 3)
    symb = oplist[opnum]

    return symb

#lists where we store x, y, and symb
xlist = []
ylist = []
symblist = []


#define equation for contents of problem loop
def probloop(loopcount, newcorrect):
    
    if newcorrect == 0:
        #generate random operation symbol
        symb = randop()
        symblist.append(symb)
    if newcorrect == 1:
        symb = symblist[-1]

    #oh cool, you could use lambda to choose operations!
    #now, i don't REALLY know how to do this, i just stole this from some person on the internet
    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y
          }

    #depending on whether you've run the loop before... maybe generating & storing? maybe taking from list?
    if newcorrect == 0:
        x = random.randrange(1, 6)
        xlist.append(x)
    if newcorrect == 1:
        x = xlist[-1]
    if newcorrect == 0:
        y = random.randrange(1, 6)
        ylist.append(y)
    if newcorrect == 1:
        y = ylist[-1]

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

    #initialize newcorrect
    newcorrect = 0

    #display results; modify correct count
    if userans == compans:
        print(f'user answer({userans}) is correct.')
        newcorrect = 1
    elif userans != compans:
        print(f'user answer({userans}) is incorrect. try again!')

    return newcorrect

#define main
def main():
    #ask user for their name
    name = input('please enter your name: ')

    #initialize correct
    correct = 0

    #loop to generate 10 random math equations
    for loopcount in range(0, 10):
        newcorrect = 0
        newcorrect = probloop(loopcount, newcorrect)
        correct = correct + newcorrect
        while newcorrect == 0:
            newcorrect = 1
            newcorrect = probloop(loopcount, newcorrect)

    #print overall results
    print(f'\n{name} answered {correct} out of 10 questions correctly.\n')

main()

    
    


