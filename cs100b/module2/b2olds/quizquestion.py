import random

class QuizQuestion:
    #how about i keep my lists up here? does that work?
    def __init__(self, xlist, ylist, symblist):
        self.xlist = xlist
        self.ylist = ylist
        self.symblist = symblist

    #define equation for contents of problem loop
    #oh, of course, you need to put self as an argument!!!
    #so maybe we're going to pass x and y in from main, and then xlist & ylist are internal
    def get_compans(self, repeat, x, y):   
        
        op = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
        } 

        #depending on whether you've run the loop before, generate & store x & y, or take from list
        if repeat == 0:
            self.xlist.append(x)
            self.ylist.append(y)
        if repeat == 1:
            x = self.xlist[-1]
            y = self.ylist[-1]

        #solve equation
        compans = op[str(self.symblist[-1])](x,y)

        #return computer answer & info on whether or not to repeat the problem
        eqtuple = (compans, repeat)
        return eqtuple

    def get_userans(self, loopcount, x, y, compans):
        #print equation
        valid = False
        while valid == False:
            try:
                userans = int(input(f'\n{(loopcount + 1)}. {x} {self.symblist[-1]} {y} = '))
                if userans == '':
                    raise ValueError('empty input')
                valid = True
            except ValueError:
                print('invalid input')

        if userans == compans:
            print(f'user answer({userans}) is correct.')
            #this still seems kind of muddled in here, with all the repeats
            newcorrect = 1
        elif userans != compans:
            print(f'user answer({userans}) is incorrect.')
            newcorrect = 0
            show = input('press 1 to see the correct answer, or any other key to continue.')
            if show == '1':
                print(f'computer answer: {x} {self.symblist[-1]} {y} = {compans}')

        return newcorrect