import random

#copy pastey let's go!!!!!
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

#ask user for name
name = input('what is your name?')

#use random module for the equations! ohhh...
#right, but then, you'd need to convert the equation strings into ints in order to solve!
#how do you do that?
#are we not solving yet?

#the fact that the next question is 'if they got it right', does that mean we SHOULD solve them?
#oh wait, i get it, the uh, algebraic type equations i was using before won't work

#create list of random operators
operators = ['+', '-', '*', '/', '%']
#keep count of correct answers
correct = 1
#generating equations
#this range still managed to surprise me
#need to ask what the best range is
for x in range(1, 10):
    rand1 = random.randrange(1, 10)
    rand2 = random.randrange(1, 10)
    operator = operators[random.randrange(0, 5)]
    #for now, i'm just going to subtract for all problems
    #that way, you can at least get negative numbers, right? that's kind of exciting?
    #calculate actual answer with variables
    answer = rand1 - rand2
    print(f'{rand1} - {rand2} = ')
    #now, what is the best way to convert an operator string to an actual operator???
    #this is the question...
    #anyway, get user answer from input
    user_ans = int_input_function()
    #see whether user answer = actual answer
    if user_ans == answer:
        print('correct')
        #increment correct if correct
        correct += 1
    else:
        print('incorrect')

#display results
print(f'you solved {correct} problems correctly')



