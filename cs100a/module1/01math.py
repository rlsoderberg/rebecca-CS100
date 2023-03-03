import sys
sys.path.append('../..')

from i import maine

import random

def int_gen():
    return random.randint(0, 9)

def float_gen():
    return random.uniform(0, 9.9)

def correctness(guess, prob_num):
    if int_vars[prob_num] == guess:
        return 1
    elif int_vars[prob_num] != guess:
        return 2
    
#very much correctness
def get_answer(x, prob_num):
    print(x + " = ")
    type = "string"
    antiblanky = 1
    guess = maine(type, antiblanky)
    correct = correctness(guess, prob_num)
    return correct

#what is going on right here with these variables?????
def guess_variable(prob_num):
    print("which variable do you wish to guess? x, y, or z?")
    #make a filter for letters other than x, y, or z
    type = "string"
    antiblanky = 1
    var_letter = maine(type, antiblanky)
    if var_letter == "x":
        correctness = get_answer(x, prob_num)
        return correctness
    elif var_letter == "y":
        correctness = get_answer(y, prob_num)
        return correctness
    elif var_letter == "z":
        correctness = get_answer(z, prob_num)
        return correctness

#4. ok, i passed prob_num all the way up to correctness, because it looks like that might be my <secret number>
def int_prob(int_vars, prob_num):
    print("Problem "+prob_num+": "+op_names[prob_num])
    x = int_vars[0]
    y = int_vars[1]
    z = int_vars[2]
    solution = prob_eqs[prob_num]
    print(prob_strings[prob_num] + "= "+ solution)
    choose_path = 1
    correct_count = 0
    while choose_path == 1:
        print("press 1 to guess a variable, and press 2 to continue to the next operation")
        type = "int"
        antiblanky = 1
        choose_path = maine(type, antiblanky)
        if choose_path == 1:
            correctness = guess_variable(prob_num)
            if (correctness == 1):
                correct_count += 1
        elif choose_path == 2:
            #exit
    #why doesn't it like my prob_num?
    prob_num += 1
        
#3. i have these, like, peripheral functions generating random ints. as well as the int_gens up there, which are feeding them.
def int_array(int_vars):
    for n in range(0, 3):
        rand_int = int_gen()
        int_vars.append(rand_int)
        n+=1
    return int_vars

#2. here i am, picking a type, and sending to int_prob. i am sending up my empty int array, int_vars
def type_select(var_type, int_vars, float_vars):
    int_vars = int_array()
    if var_type == "int":
        int_prob(int_vars)


var_type = "int"
prob_num = 1
int_vars = []
float_vars = []
prob_strings = ["x + y + x","z - y - x","x * y * z","(x+y)/z","(y-z)%x","x**z+y**z"]
prob_eqs = [x + y + x,z - y - x,x * y * z,(x+y)/z,(y-z)%x,x**z+y**z]
op_names = ["0", "Addition", "Subtraction","Multiplication","Division","Modulo","Exponent"]
rand_int = 0
rand_float = 0
#1. i am starting this off by picking a type (although i only have int going right now)
type_select(var_type, int_vars, float_vars)