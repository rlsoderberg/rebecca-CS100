import sys
sys.path.append('../..')

from i import input_function

import random
from sympy import symbols, Eq, solve

def correctness_display(abc, letter_pair, correct_count, op_num):
    var_select = letter_pair[0]
    if (abc[var_select] == letter_pair[1]):
        correct_count += 1
        print("correct!")
        print("correct answers: "+str(correct_count)+" out of 3")
    elif (abc[var_select] != letter_pair[1]):
        print("incorrect!")
        print("correct answers: "+str(correct_count)+" out of 3")


def letter_guess():
    print("which variable do you wish to guess? x, y, or z?")
    type_name = "string"
    var_select = "a"
    while var_select != 'x' and var_select != 'y' and var_select != 'z':
        var_select = input_function(type_name)
    letter_pair = (0,'f')
    if var_select == "x":
        type = "int"
        print("int x =")
        letter_pair = (0, input_function(type_name))
    elif var_select == "y":
        type = "int"
        print("int y =")
        letter_pair = (1, input_function(type_name))
    elif var_select == "z":
        type = "int"
        print("int z =") 
        letter_pair = (2, input_function(type_name))
    return letter_pair


def prob_display(prob_strings, solution, op_names, op_num):
    print("Operation "+str(op_num + 1)+": "+op_names[op_num])
    print(str(prob_strings[op_num]) + " = "+ str(solution))    

    print("press 1 to guess a variable")
    print("press 2 to return to the main menu")
    type_name = "int"
    path_var = 0
    while path_var < 1 or path_var > 2:
        path_var = int(input_function(type_name))
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
    abc = intgen_abc(abc)
    solutions = []
    solutions = correct_answers(prob_eqs, abc, solutions, op_num)
    path_var = prob_display(prob_strings, solutions, op_names, op_num) 
    while path_var == 1:
        letter_pair = letter_guess()
        correctness_display(abc, letter_pair, correct_count, op_num)
        print("press 1 to guess another variable for this operation, or 2 to return to main menu.")
        type_name = "int"
        path_var = 0
        while path_var < 1 or path_var > 2:
            path_var = input_function(type_name)
    op_num += 1
    return correct_count

def operation_select(correct_count):
    print("welcome to GUESS THE VARIABLE")
    print("type a symbol to pick an operation:")
    print("1. + addition   2. - subtraction   3. * multiplication   4. / division   5. % modulo   6. ^ exponent")
    type_name = "string"
    op_input = "0"
    while op_input != "+" and op_input != "-" and op_input != "*" and op_input != "/" and op_input != "%" and op_input != "^":
        op_input = input_function(type_name)
    #look at all this copy and pasting!!!!!! aaaaaaaaaaa
    #also what even are integers and floats?
    if op_input == "+":
        correct_count = problem(0, abc, prob_strings, prob_eqs, op_names)
    elif op_input == "-":
        correct_count = problem(1, abc, prob_strings, prob_eqs, op_names)
    elif op_input == "*":
        correct_count = problem(2, abc, prob_strings, prob_eqs, op_names)
    elif op_input == "/":
        correct_count = problem(3, abc, prob_strings, prob_eqs, op_names)
    elif op_input == "%":
        correct_count = problem(4, abc, prob_strings, prob_eqs, op_names)
    elif op_input == "^":
        correct_count = problem(5, abc, prob_strings, prob_eqs, op_names)
    return correct_count

op_num = 0
abc = []
prob_strings = ["x + 2*y + 3*z = ","z - y - x = ","x*y*z","(x+y)/z","(y-z)%x","x**z+y**z"]
x, y, z = symbols('x y z')
prob_eqs = [(x + 2*y + 3*z),(2*z - y - 3*x),(x * y * z),((x+y)/z),((y-z)%x),(x**z+y**z)]
op_names = ["Addition", "Subtraction","Multiplication","Division","Modulo","Exponent"]

correct_count = 0
while correct_count < 3:
    correct_count = operation_select(correct_count)
if correct_count == 3:
    print("congratulations! you guessed all three variables!")