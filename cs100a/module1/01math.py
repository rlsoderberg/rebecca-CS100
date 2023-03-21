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


def letter_guess():
    print("which variable do you wish to guess? x, y, or z?")
    type = "string"
    antiblanky = 1
    var_to_guess = maine(type, antiblanky)
    while var_to_guess != 'x' and var_to_guess != 'y' and var_to_guess != 'z':
        var_to_guess = maine(type, antiblanky)
    letter_pair = (0,0)
    var_letter = maine(type, antiblanky)
    if var_letter == "x":
        print("x = ")
        letter_pair[0] = 0
        letter_pair[1] = maine(type, antiblanky)
    elif var_letter == "y":
        print("y = ")
        letter_pair[0] = 1
        letter_pair[1] = maine(type, antiblanky)
    elif var_letter == "z":
        letter_pair[0] = 2
        letter_pair[1] = maine(type, antiblanky)
    return letter_pair


def prob_display(abc, prob_strings, solution, op_names):
    print("Problem "+prob_strings+": "+op_names[prob_num])
    a = abc[0]
    b = abc[1]
    c = abc[2]
    print(prob_strings[prob_num] + "= "+ solution)
    choose_path = 1
    correct_count = 0
    print("press 1 to guess a variable, and press 2 to continue to the next operation")
    type = "int"
    antiblanky = 1
    path_var = maine(type, antiblanky)
    return path_var

def correct_answers(prob_eqs, prob_num, abc):
    for b in abc:
        #i don't think i'm transferring these symbols right, and i don't know if sympy is the best way to do this
        x, y, z = symbols('x y z')
        d = abc[b]
        solution = solve(d)
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


prob_num = 1
prob_count = 1
abc = []
prob_strings = ["x + y + x","z - y - x","x * y * z","(x+y)/z","(y-z)%x","x**z+y**z"]
x, y, z = symbols('x y z')
prob_eqs = [(x + y + x),(z - y - x),(x * y * z),((x+y)/z),((y-z)%x),(x**z+y**z)]
op_names = ["0", "Addition", "Subtraction","Multiplication","Division","Modulo","Exponent"]
total_questions = 6

while total_questions > 0:
    correct_count = 0
    abc.clear()
    if total_questions >= 3:
        abc = intgen_abc(abc)
    elif total_questions < 3:
        abc = floatgen_abc(abc)
    solution = correct_answers(prob_eqs, prob_num, abc)
    path_var = prob_display(abc, prob_strings, solution, op_names)
    while path_var == 1:
        letter_pair = letter_guess()
        correctness = check_answer(abc, letter_pair, solution)
        correctness_display(correct_count, correctness)
    prob_num += 1
    prob_count += 1
    total_questions -= 1
