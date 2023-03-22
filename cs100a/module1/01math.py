import sys
sys.path.append('../..')

from i import maine

import random
import sympy
from sympy import symbols, Eq, solve

def correctness_display(correct_count, correctness, prob_count):
    if (correctness == 1):
        correct_count += 1
        print("correct!")
        print("correct answers: "+correct_count+" out of "+prob_count)
    elif (correctness != 1):
        print("incorrect!")
        print("correct answers: "+correct_count+" out of "+prob_count)

def check_answer(abc, letter_pair, solution):
    abc_num = letter_pair[0]
    if abc[abc_num] == solution:
        correctness = 1
    return correctness


def letter_guess(intfloat):
    print("which variable do you wish to guess? x, y, or z?")
    type = "str"
    antiblanky = 1
    var_select = maine(type, antiblanky)
    while var_select != 'x' and var_select != 'y' and var_select != 'z':
        var_select = maine(type, antiblanky)
    letter_pair = (0,'f')
    var_letter = maine(type, antiblanky)
    if var_letter == "x":
        if intfloat == 0:
            print("INT x = ")     
        if intfloat == 1:
            print("FLOAT x = ") 
        letter_pair[0] = 0
        letter_pair[1] = maine(type, antiblanky)
    elif var_letter == "y":
        if intfloat == 0:
            print("INT y = ")     
        if intfloat == 1:
            print("FLOAT y = ") 
        letter_pair[0] = 1
        letter_pair[1] = maine(type, antiblanky)
    elif var_letter == "z":
        if intfloat == 0:
            print("INT z = ")     
        if intfloat == 1:
            print("FLOAT z = ") 
        letter_pair[0] = 2
        letter_pair[1] = maine(type, antiblanky)
    return letter_pair


def prob_display(prob_strings, solution, op_names, prob_num):
    print("Problem "+str(prob_num + 1)+": "+op_names[prob_num])
    print(str(prob_strings[prob_num]) + " = "+ str(solution[prob_num]))
    choose_path = 1
    correct_count = 0

    print("press 1 to guess")
    print("press 2 to continue to the next equation")
    antiblanky = 1
    type = "int"
    path_var = 0
    while path_var < 1 or path_var > 2:
        path_var = maine(type, antiblanky)
    return path_var

def correct_answers(prob_eqs, abc, solution):
    x = abc[0]
    y = abc[1]
    z = abc[2]
    for b in abc:
        #list index out of range . is sympy the right way to do this?????
        x, y, z = symbols('x y z')
        solution.append(solve(prob_eqs))
    
    return solution

def floatgen_abc(abc):
    for n in range(0, 3):
        rand_float = random.uniform(0,9.9)
        abc.append(rand_float)
        n+=1
    return abc

def intgen_abc(abc):
    for n in range(0, 3):
        rand_int = random.randint(0,10)
        abc.append(rand_int)
        n+=1
    return abc


prob_num = 0
abc = []
prob_strings = ["x + y + x","z - y - x","x * y * z","(x+y)/z","(y-z)%x","x**z+y**z"]
x, y, z = symbols('x y z')
prob_eqs = [(x + y + x),(z - y - x),(x * y * z),((x+y)/z),((y-z)%x),(x**z+y**z)]
op_names = ["Addition", "Subtraction","Multiplication","Division","Modulo","Exponent"]
total_questions = 6
#this seems somewhat inefficient!!!

while total_questions > 0:
    correct_count = 0
    abc.clear()
    if total_questions >= 3:
        intfloat = 0
        abc = intgen_abc(abc)
    elif total_questions < 3:
        intfloat = 1
        abc = floatgen_abc(abc)
    solution = []
    solution = correct_answers(prob_eqs, abc, solution)
    path_var = prob_display(prob_strings, solution, op_names, prob_num) 
    while path_var == 1:
        letter_pair = letter_guess(intfloat)
        correctness = check_answer(abc, letter_pair, solution)
        correctness_display(correct_count, correctness)
    total_questions -= 1
    prob_num += 1