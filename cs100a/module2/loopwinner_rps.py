#4

#oh, right, i had it looping, but i had no winner! well, it will be over there, number 13

#5

#well, this one is also rps-related. maybe i'll just make a new copy over here.


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

#list of play names
rps = [0, 'rock', 'scissors', 'paper']
#i know there will have to be a big turn loop here!

#coming in from module 2 number 4, and i'd better initialize some point variables first!
user_pts = 0
comp_pts = 0

#we are putting in a for loop for a set number of rounds
roundcount = 0
winner = 0
#welcome user to program
print('\nwelcome to rock paper scissors')

#using a while loop, because it's easier to keep track of roundcount that way
while roundcount < 7:

    #announce round
    print(f'\nround {roundcount+1}')

    #so we're going to have another loop in here, making sure no ties
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

    #remember to reset winner!
    winner = 0        
    roundcount += 1

print(f'you won {user_pts} times and computer won {comp_pts} times.')
if user_pts > comp_pts:
    print('you are the rock paper scissors champion!')
elif user_pts < comp_pts:
    print('computer is the rock paper scissors champion!')
elif user_pts > comp_pts:
    print('you reach a grand tie with computer!')

