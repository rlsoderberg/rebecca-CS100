#import random, to determine computer plays
import random

#define input function
def int_input_function():
    valid = False
    while valid == False:
        try: 
            result = int(input())
            if result == '':
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print('Invalid Input')
    return result

#randrange is unevenly inclusive, like normal range

#list of play names
rps = [0, 'rock', 'scissors', 'paper']

#big turn loop plays until exit
exit = False
while exit == False:
    #computer play determined by random
    comp = random.randrange(1, 4)
    #user inputs their play
    #switched the order of rock paper scissors
    print('will you play 1. rock, 2. scissors, or 3. paper?')
    user = int_input_function()

    #display results of player vs. computer
    if user == comp:
        print(f'you played {rps[user]}, and computer played {rps[comp]}. tie!')

    #display results 
    print(f'you played {rps[user]} and computer played {rps[comp]}.')
    if (user - comp == -1) or (user - comp == 2):
        print('you win!')
    elif (user - comp == 0):
        print('tie!')
    else:
        print('you lose!')

    #request for user to continue/exit    
    input('press any key to continue, or x to exit')
