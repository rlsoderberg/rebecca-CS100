#right, rock paper scissors, this was a funny little thing, wasn't it?
#now how did it go...

#importing random, do determine computer plays
import random
#let's also import the input function from 11_12
#from 11_12 import int_input_function what, this is getting all underlined???
#ohhhh, you can only do that with CLASSES, can't you...
#looks like it's time for a little copy pastey
def int_input_function():
    valid = False
    while valid == False:
        try: 
            result = int(input())
            #oh i'd better put in the empty string catcher
            #oh wait, there was an error when i said 'if not result', and i made one of the variables 0
            #so i think i prefer "if result == '' "???
            if result == '':
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print('Invalid Input')
    return result

#is randrange weird like range??? here is where we shall test
"""for x in range(0, 7):
    comp = random.randrange(0, 3)
    print(comp)"""
#i think we have indeed concluded that randrange is just as weird

#list of play names
rps = [0, 'rock', 'scissors', 'paper']
#i know there will have to be a big turn loop here!
exit = False
while exit == False:
    #computer play determined by random
    comp = random.randrange(1, 4)
    #user inputs their play
    print('will you play 1. rock, 2. scissors, or 3. paper?')
    user = int_input_function()

    #right, so was the thing that i had to figure out each play individually?
    #is there any way around this???
    if user == comp:
        print(f'you played {rps[user]}, and computer played {rps[comp]}. tie!')

    #well, i'm trying to come up with a little algorithm for this, and that's right
    #rock paper scissors is the wrong order!!!

    #right, so let's test this, and see what the differences are
    """    print(f'you played {rps[user]} and computer played {rps[comp]}.')
    print(f'user:{user} - comp:{comp} = {user - comp}')
    print('press any key to continue, or x to exit')"""

    #well, there's a pattern that works, where you win with user - comp = -1 or 2, and you lose with 1 or -2
    #like, it makes sense, but i totally would not have come up with that!!!!
    
    print(f'you played {rps[user]} and computer played {rps[comp]}.')
    if (user - comp == -1) or (user - comp == 2):
        print('you win!')
    elif (user - comp == 0):
        print('tie!')
    else:
        print('you lose!')
        
    input('press any key to continue, or x to exit')

