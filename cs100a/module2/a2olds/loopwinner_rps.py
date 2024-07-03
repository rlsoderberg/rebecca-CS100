#importing random, to determine computer plays
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

#list of play names
rps = [0, 'rock', 'scissors', 'paper']

#initialize point variables
user_pts = 0
comp_pts = 0

#initialize round count and winner variables
roundcount = 0
winner = 0

#welcome user to program
print('\nwelcome to rock scissors paper')

#using a while loop, to keep track of round count
while roundcount < 7:

    #announce round
    print(f'\nround {roundcount+1}')

    #another loop in here, playing until winner (no ties)
    while winner == 0:
        #computer play determined by random
        comp = random.randrange(1, 4)
        #user inputs their play
        print('will you play 1. rock, 2. scissors, or 3. paper?')
        user = int_input_function()

        #calculate results
        print(f'you played {rps[user]} and computer played {rps[comp]}.')
        if (user - comp == -1) or (user - comp == 2):
            print('you win!')
            user_pts += 1
            winner = 1
        elif (user - comp == 0):
            print('tie! we are repeating this round.')
        else:
            print('you lose!')
            comp_pts += 1
            winner = 1

    #remember to reset winner, and increase round count, after completing a round
    winner = 0        
    roundcount += 1

#display match results
print(f'you won {user_pts} times and computer won {comp_pts} times.')
if user_pts > comp_pts:
    print('you are the rock scissors paper champion!')
elif user_pts < comp_pts:
    print('computer is the rock scissors paper champion!')
elif user_pts > comp_pts:
    print('you reach a grand tie with computer!')

