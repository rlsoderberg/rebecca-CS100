import sys
sys.path.append('../..')

from i import maine

import random


def correctness_display(correct_count, correctness, prob_count):
    if (correctness == 1):
        correct_count += 1
        print("correct!")
        print("correct answers: "+correct_count+" out of "+prob_count)
    elif (correctness != 1):
        print("incorrect!")
        print("correct answers: "+correct_count+" out of "+prob_count)

def check_answer(xyz, letter_pair, solution):
    xyz_num = letter_pair[0]
    if xyz[xyz_num] == solution:
        correctness = 1
    return correctness


def letter_guess():
    print("which variable do you wish to guess? x, y, or z?")
    #make a filter for letters other than x, y, or z
    type = "string"
    antiblanky = 1
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


def prob_display(xyz, prob_strings, solution, op_names):
    print("Problem "+prob_strings+": "+op_names[prob_num])
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    print(prob_strings[prob_num] + "= "+ solution)
    choose_path = 1
    correct_count = 0
    print("press 1 to guess a variable, and press 2 to continue to the next operation")
    type = "int"
    antiblanky = 1
    path_var = maine(type, antiblanky)
    return path_var

def correct_answers(prob_eqs, prob_num, xyz):
    for x in xyz:
        d = xyz[x]
        #don't know how to do this
        solution = prob_eqs[prob_num]<d>
    return solution

#does this work, passing back arrays like this???
def intgen_xyz(prob_num):
    for n in range(0, 3):
        rand_int = random.randint(0,10)
        xyz.append(rand_int)
        n+=1
    return xyz


prob_num = 1
prob_count = 1
xyz = []
prob_strings = ["x + y + x","z - y - x","x * y * z","(x+y)/z","(y-z)%x","x**z+y**z"]
#hmmmmmmmmm, how am i going to write these equations????
prob_eqs = [x + y + x,z - y - x,x * y * z,(x+y)/z,(y-z)%x,x**z+y**z]
op_names = ["0", "Addition", "Subtraction","Multiplication","Division","Modulo","Exponent"]
correct_answers(prob_eqs)
#this does not seem like an efficient way to do this!!!
int_question_count = 3
float_question_count = 3
for x in int_question_count:
    path_var = 1
    type = "int"
    correct_count = 0
    xyz = intgen_xyz(prob_num)
    solution = correct_answers(prob_eqs, prob_num, xyz)
    path_var = prob_display(xyz, prob_strings, solution, op_names)
    while path_var == 1:
        letter_pair = letter_guess()
        correctness = check_answer(xyz, letter_pair, solution)
        correctness_display(correct_count, correctness)
    prob_num += 1
    prob_count += 1
#pretend there is another one down here for float_questions
