import sys
sys.path.append('../..')

from i import input_function

import random
from sympy import symbols, Eq, solve

def correctness_display(correct_count, correctness, prob_count):
    if (correctness == 1):
        correct_count += 1
        print("correct!")
        print("correct answers: "+correct_count+" out of "+prob_count)
    elif (correctness != 1):
        print("incorrect!")
        print("correct answers: "+correct_count+" out of "+prob_count)

def check_answer(abc, letter_pair, solutions):
    abc_num = letter_pair[0]
    if abc[abc_num] == solutions:
        correctness = 1
    return correctness


def letter_guess():
    print("which variable do you wish to guess? x, y, or z?")
    type = "str"
    antiblanky = 1
    var_select = input_function(type, antiblanky)
    while var_select != 'x' and var_select != 'y' and var_select != 'z':
        var_select = input_function(type, antiblanky)
    letter_pair = (0,'f')
    var_letter = input_function(type, antiblanky)
    if var_letter == "x":
        print("int x =")
        letter_pair[0] = 0
        letter_pair[1] = input_function(type, antiblanky)
    elif var_letter == "y":
        print("int y =")
        letter_pair[0] = 1
        letter_pair[1] = input_function(type, antiblanky)
    elif var_letter == "z":
        print("int z =") 
        letter_pair[0] = 2
        letter_pair[1] = input_function(type, antiblanky)
    return letter_pair


def prob_display(prob_strings, solution, op_names, prob_num):
    print("Problem "+str(prob_num + 1)+": "+op_names[prob_num])
    print(str(prob_strings[prob_num]) + " = "+ str(solution))    
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

def correct_answers(prob_eqs, abc, solutions, prob_num):
    expr = prob_eqs[prob_num]
    a = abc[0]
    b = abc[1]
    c = abc[2]
    print(a)
    print(b)
    print(c)
    x, y, z = symbols('x y z')
    solution = expr.subs(x, a).subs(y, a).subs(z,a)


    solutions.append(solution)
    
    return solutions

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
prob_strings = ["2*x + yz = ","z - y - x = ","x * y * z","(x+y)/z","(y-z)%x","x**z+y**z"]
x, y, z = symbols('x y z')
prob_eqs = [(x + y + x),(z - y - x),(x * y * z),((x+y)/z),((y-z)%x),(x**z+y**z)]
op_names = ["Addition", "Subtraction","Multiplication","Division","Modulo","Exponent"]
total_questions = 6

while total_questions > 0:
    correct_count = 0
    abc.clear()
    #need to distinguish between int abc and floatgen abc, will do later
    abc = intgen_abc(abc)
    solutions = []
    solutions = correct_answers(prob_eqs, abc, solutions, prob_num)
    path_var = prob_display(prob_strings, solutions, op_names, prob_num) 
    while path_var == 1:
        letter_pair = letter_guess()
        correctness = check_answer(abc, letter_pair, solutions)
        correctness_display(correct_count, correctness)
    total_questions -= 1
    prob_num += 1
    #actually, prob_num needs to be op_num, which counts to 6 and then prob_num changes, but i'll leave this for now 