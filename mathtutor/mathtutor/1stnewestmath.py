import random

#define problem function
def problem(problems_list, x):
    rand1 = random.randrange(1, 10)
    rand2 = random.randrange(1, 10)
    operator = operators[random.randrange(0, 5)]
    #for now, i'm just going to subtract for all problems
    #that way, you can at least get negative numbers, right? that's kind of exciting?
    #calculate actual answer with random variables
    answer = rand1 - rand2
    print(f'{rand1} - {rand2} = ')
    #WAT IS BEST WAY TO SAVE STRING?
    #i guess this works
    #make it have the right variable types
    problem_string = str(rand1) + " - " + str(rand2) + ' = '

    #now, what is the best way to convert an operator string to an actual operator???
    #this is the question...
    #anyway, get user answer from input
    user_ans = int_input_function()

    #see whether user answer = actual answer
    if user_ans == answer:
        print('correct')
        #increment correct if correct
        correct = 1
    else:
        print('incorrect')
        correct = 0

    #put problem number, equation, answer, user_ans, & correct in a tuple
    problem_item = (x, problem_string, answer, user_ans, correct)
    problems_list.append(problem_item)


#copy pastey let's go!!!!!
#hey i'm editing this tomorrow, now shame shame shame, practice u writing the input function
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
name = input('what is your name? ')

#use random module for the equations! ohhh...
#right, but then, you'd need to convert the equation strings into ints in order to solve!
#how do you do that?
#are we not solving yet?

#the fact that the next question is 'if they got it right', does that mean we SHOULD solve them?
#oh wait, i get it, the uh, algebraic type equations i was using before won't work

#create list of random operators
operators = ['+', '-', '*', '/', '%']
#keep count of correct answers
#why did i have correct = 1??? i don't get it
total_correct = 0
#generating equations
#this range still managed to surprise me
#need to ask what the best range is

#initialize problems_list
problems_list = []
for x in range(1, 10):
    problem(problems_list, x)
    current_problem = problems_list[-1]
    (n, p , a, u, c) = current_problem
    #OH!!! it works because current_problem is the same thing as current_problem, and you unpack it
    correct = c
    total_correct += correct

#display results
print(f'you solved {total_correct} out of 10 problems correctly')

#give user preparation before hitting them with the problems list
input('press any key to see your full results')
for x in problems_list:
    (n, p, a, u, c) = x
    if c == 1:
        correct = 'correct'
    else:
        correct = 'incorrect'
    print(f"problem {n}: {p}. correct answer: {a}. user answer: {u}. {correct}")





