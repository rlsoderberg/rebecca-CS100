import sys
sys.path.append('../..')

from i import input_function

import random
import sympy
from sympy import symbols, Eq, solve, sympify

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
    var_select = input_function(type, antiblanky)
    while var_select != 'x' and var_select != 'y' and var_select != 'z':
        var_select = input_function(type, antiblanky)
    letter_pair = (0,'f')
    var_letter = input_function(type, antiblanky)
    if var_letter == "x":
        if intfloat == 0:
            print("INT x = ")     
        if intfloat == 1:
            print("FLOAT x = ") 
        letter_pair[0] = 0
        letter_pair[1] = input_function(type, antiblanky)
    elif var_letter == "y":
        if intfloat == 0:
            print("INT y = ")     
        if intfloat == 1:
            print("FLOAT y = ") 
        letter_pair[0] = 1
        letter_pair[1] = input_function(type, antiblanky)
    elif var_letter == "z":
        if intfloat == 0:
            print("INT z = ")     
        if intfloat == 1:
            print("FLOAT z = ") 
        letter_pair[0] = 2
        letter_pair[1] = input_function(type, antiblanky)
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
        path_var = input_function(type, antiblanky)
    return path_var

def correct_answers(prob_strings, abc, solution, prob_num):
    expr = prob_eqs[prob_num]
    a = abc[0]
    b = abc[1]
    c = abc[2]
    print(a)
    print(b)
    print(c)
    for b in abc:
        x, y, z = symbols('x y z')
        expr.subs({x:a, y:b, z:c})
        solution.append(expr)
    
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
#is there a better way to do this than sympy?????
prob_strings = ["x + y + x = ","z - y - x = ","x * y * z","(x+y)/z","(y-z)%x","x**z+y**z"]
x, y, z = symbols('x y z')
prob_eqs = [(x + y + x),(z - y - x),(x * y * z),((x+y)/z),((y-z)%x),(x**z+y**z)]
op_names = ["Addition", "Subtraction","Multiplication","Division","Modulo","Exponent"]
total_questions = 6

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
    solution = correct_answers(prob_strings, abc, solution, prob_num)
    path_var = prob_display(prob_strings, solution, op_names, prob_num) 
    while path_var == 1:
        letter_pair = letter_guess(intfloat)
        correctness = check_answer(abc, letter_pair, solution)
        correctness_display(correct_count, correctness)
    total_questions -= 1
    prob_num += 1