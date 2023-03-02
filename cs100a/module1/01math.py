import sys
sys.path.append('../..')

from i import maine

import random

def int_gen():
    return random.randint(0, 9)

def float_gen():
    return random.uniform(0, 9.9)

def problem(prob_num, prob_vars,prob_eqs,op_names,rand_int,rand_float, var_type):
    print("Problem "+prob_num+": "+op_names[prob_num])

    if var_type == "int":
        x = int_vars[0]
        y = int_vars[1]
        z = int_vars[2]
    elif var_type == "float":
        x = float_vars[0]
        y = float_vars[1]
        z = float_vars[2]
    #you see how, right here, i'm actually trying to plug stuff into the equation??? how do i do that???
    solution = prob_eqs[prob_num]
    print(prob_strings[prob_num] + "= "+ solution)
    print("press 1 to guess a variable, and press 2 to continue to the next operation")
    type = "int"
    antiblanky = 1
    action = maine(type, antiblanky)
    if action == 1:
        print("would you like to guess x, y, or z?")
        type = "string"
        antiblanky = 1
        #how do i do it so they choose a letter, and it marks which letter they picked (and the number it correlates with)????
        <secret-number>guess_letter = maine(type, antiblanky)
        print(guess_letter+"= ")
        type = "float"
        antiblanky = 1
        guess_input = maine(type, antiblanky)
        if guess_input == <secret-number>rand_int



    prob_num +=1

def int_prob(int_vars):
    print("Problem "+prob_num+": "+op_names[prob_num])
    x = int_vars[0]
    y = int_vars[1]
    z = int_vars[2]
    solution = prob_eqs[prob_num]
    print(prob_strings[prob_num] + "= "+ solution)
    print("press 1 to guess a variable, and press 2 to continue to the next operation")
    type = "int"
    antiblanky = 1
    var_select = maine(type, antiblanky)
    guess_check(var_select, int_vars)

def int_array():
    for n in range(0, 3):
        rand_int = int_gen()
        int_vars.append(rand_int)
        n+=1

def float_array():
    for n in range(0, 3):
        longfloat = float_gen()
        rand_float = round(longfloat, 1)
        float_vars.append(rand_float)
        n+=1

def type_select(var_type, int_vars, float_vars):
    if var_type == "int"
        int_prob(int_vars)
    elif var_type == "float"
        float_prob(float_vars)

var_type = "int"
prob_num = 1
int_vars = []
float_vars = []
#also why does %x always turn blue?
prob_strings = ["x + y + x","z - y - x","x * y * z","(x+y)/z","(y-z)%x","x**z+y**z"]
prob_eqs = [x + y + x,z - y - x,x * y * z,(x+y)/z,(y-z)%x,x**z+y**z]
op_names = ["Addition", "Subtraction","Multiplication","Division","Modulo","Exponent"]
rand_int = 0
rand_float = 0















"""
def check(s):
    #how do i pick which variable i am checking????
    print("press 1 to guess a variable, and press 2 to continue to the next operation")
    action = maine(type, antiblanky)
    while action == 1: #is this even the right way to do it???
        guess = maine(type, antiblanky)
        if guess == #the right answer?????:
            print("Correct!")
        elif guess != #the right answer?????:
            print("Incorrect!")
        print("press 1 to guess a variable, and press 2 to continue to the next operation")
        action = maine(type, antiblanky)




def label(count):
    count += 1
    print("Operation "+count+": ")




#welcome users to math.py
print("Welcome to math.py. \n Can you guess the variables?")

#create int variables
x = 7
y = 4
z = 26

#create float variables
a = 9.3
b = 2.6
c = 15.7

#perform arithmetic operations on int variables
sum = x + y + z
difference = z - y - x
product = x * y * z
quotient = (x + y) / z
mod = (y-z)%x
power = x**z + y**z

count = 0

#display arithmetic operations for int variables
print("1. Arithmetic operations performed on "+ type(x)+ "variable")
label(count)
print("x + y + z = ", sum)
check(s) #see, what i need to do, is put the variables in, like, a set or something? maybe also make them so i can referece them? idk!!!
#and also, i need to be looping through the problems!!!
# AND i need to tidy up my input function!!!
print("x - y - z = ", difference)
print("x * y * z = ", product)
print("(x + y)/z = ", quotient)
print("(y - z) % x = ", mod)
print("x**z + y**z = ", power)

#perform arithmetic operations on float variables
sum = x + y + z
difference = x - y - z
product = x * y * z
quotient = (x + y)/z
mod = (y - z) % x
power = x**z + y**z

count = 0



#display arithmetic operations for float variables
print("1. Arithmetic operations performed with "+ type(a))+ "variable")
print("x - y - z = ", difference)
print("x * y * z = ", product)
print("(x + y)/z = ", quotient)
print("(y - z) % x = ", mod)
print("x**z + y**z = ", power)

"""
