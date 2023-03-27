import sys
sys.path.append('../..')

from i import input_function

import random
from sympy import symbols, Eq, solve

def correctness_display(abc, letter_pair, solutions, correct_count, op_num):
    a = abc[0]
    b = abc[1]
    c = abc[2]
    var_select = letter_pair[0]
    if (abc[var_select] == letter_pair[1]):
        correct_count += 1
        print("correct!")
        print("correct answers: "+str(correct_count)+" out of "+str(op_num+ 1))
    elif (abc[var_select] != letter_pair[1]):
        print("incorrect!")
        print("correct answers: "+str(correct_count)+" out of "+str(op_num + 1))


def letter_guess():
    print("which variable do you wish to guess? x, y, or z?")
    type = "string"
    antiblanky = 1
    var_select = "a"
    while var_select != 'x' and var_select != 'y' and var_select != 'z':
        var_select = input_function(type, antiblanky)
    letter_pair = (0,'f')
    if var_select == "x":
        type = "int"
        print("int x =")
        letter_pair = (0, input_function(type, antiblanky))
    elif var_select == "y":
        type = "int"
        print("int y =")
        letter_pair = (1, input_function(type, antiblanky))
    elif var_select == "z":
        type = "int"
        print("int z =") 
        letter_pair = (2, input_function(type, antiblanky))
    return letter_pair


def prob_display(prob_strings, solution, op_names, op_num):
    print("Problem "+str(op_num + 1)+": "+op_names[op_num])
    print(str(prob_strings[op_num]) + " = "+ str(solution))    
    choose_path = 1
    correct_count = 0

    print("press 1 to guess a variable")
    print("press 2 to continue to the next equation")
    antiblanky = 1
    type = "int"
    path_var = 0
    while path_var < 1 or path_var > 2:
        path_var = input_function(type, antiblanky)
    return path_var
#i just copy and pasted this thing! that's not nice???
def prob_display_review(prob_strings, solution, op_names, op_num):
    print("Problem "+str(op_num + 1)+": "+op_names[op_num])
    print(str(prob_strings[op_num]) + " = "+ str(solution))    
    choose_path = 1
    correct_count = 0

    print("press 1 to guess a variable")
    print("press 2 to return to PROBLEM REVIEW")
    antiblanky = 1
    type = "int"
    path_var = 0
    while path_var < 1 or path_var > 2:
        path_var = input_function(type, antiblanky)
    return path_var

def correct_answers(prob_eqs, abc, solutions, op_num):
    expr = prob_eqs[op_num]
    a = abc[0]
    b = abc[1]
    c = abc[2]
    x, y, z = symbols('x y z')
    solution = expr.subs(x, a).subs(y, b).subs(z,c)


    solutions.append(solution)
    
    return solutions

def floatgen_abc(abc):
    for n in range(0, 3):
        rand_float = random.uniform(0,10)
        abc.append(rand_float)
        n+=1
    return abc

def intgen_abc(abc):
    for n in range(0, 3):
        rand_int = random.randint(0,10)
        abc.append(rand_int)
        n+=1
    return abc

def problem(op_num, abc, prob_strings, prob_eqs, op_names):
    correct_count = 0
    abc.clear()
    #need to distinguish between int abc and floatgen abc, will do later
    abc = intgen_abc(abc)
    solutions = []
    solutions = correct_answers(prob_eqs, abc, solutions, op_num)
    path_var = prob_display(prob_strings, solutions, op_names, op_num) 
    while path_var == 1:
        letter_pair = letter_guess()
        correctness_display(abc, letter_pair, solutions, correct_count, op_num)
        print("press 1 to guess another variable, or 2 to return for next equation.")
        antiblanky = 1
        type = "int"
        path_var = 0
        while path_var < 1 or path_var > 2:
            path_var = input_function(type, antiblanky)
    op_num += 1
    return correct_count

op_num = 0
abc = []
prob_strings = ["2*x + y*z = ","z - y - x = ","x * y * z","(x+y)/z","(y-z)%x","x**z+y**z"]
x, y, z = symbols('x y z')
prob_eqs = [(2*x + y*z),(z - y - x),(x * y * z),((x+y)/z),((y-z)%x),(x**z+y**z)]
op_names = ["Addition", "Subtraction","Multiplication","Division","Modulo","Exponent"]

print("variables are integers between 0 and 10")
while op_num <= 6:
    correct_count = problem(op_num, abc, prob_strings, prob_eqs, op_names)
    op_num += 1
if op_num == 6:
    print("PROBLEM REVIEW")
    print("type the symbol for an operation, to review a problem.")
    #i also just copy and pasted this!!! what a mess
    abc.clear()
    abc = intgen_abc(abc)
    solutions = []
    solutions = correct_answers(prob_eqs, abc, solutions, op_num)
    path_var = prob_display_review(prob_strings, solutions, op_names, op_num) 
    while path_var == 1:
        letter_pair = letter_guess()
        correctness_display(abc, letter_pair, solutions, correct_count, op_num)
        print("press 1 to guess another variable, or 2 to return to PROBLEM REVIEW.")
        antiblanky = 1
        type = "int"
        path_var = 0
        while path_var < 1 or path_var > 2:
            path_var = input_function(type, antiblanky)
if correct_count == 3:
    print("congratulations! you guessed all three variables!")
elif correct_count < 3:
    print("you only guessed"+str(correct_count)+"variables. better luck next time!")