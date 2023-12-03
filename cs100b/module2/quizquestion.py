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
            #set x & y, depending on repeat
            while x == self.xlist[-1] and y == self.ylist[-1]:
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

    def get_userans(self, loopcount, x, y):
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

        return userans

    def display_result(self, userans, compans, repeat):
        #display results; modify correct count
        print(f'user answer = {userans} -- computer answer = {compans}')
        if userans == compans:
            print(f'user answer({userans}) is correct.')
            #this still seems kind of muddled in here, with all the repeats
            if repeat == 0:
                newcorrect = 1
                print(f'newcorrect is 1, because answer was correct on first attempt')
            repeat = 0
        elif userans != compans:
            print(f'user answer({userans}) is incorrect. try again!')
            repeat = 1
            newcorrect = 0
            print(f'newcorrect is 0, because answer was incorrect')

        return newcorrect