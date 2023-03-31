import sys
sys.path.append('../..')

from i import input_function

def int_input_function():
    valid = False
    while valid == False:
        try:
            x = int(input("x = "))
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

import random

def print_equation(lava_level, equation_strings, prob_seq, x):
    print("\ncurrent lava level: "+str(lava_level)+" feet")
    print("equation "+str(x+1))
    print(str(equation_strings[prob_seq[x]]))

#equations and correct answers
equation_strings = ["5x + 3 = 13", "14 - 3x = 2", "9 - 2x = 3", "8x + 2 = 50", "2x + 16 = 40", "12 - 2x = 2", "7 = 49 - 6x", "30 + 7x = 86", "4x + 20 = 56", "3x - 3 = 39"]
answers = [2, 4, 3, 6, 12, 5, 7, 8, 9, 14]

#request identification
print("Welcome to the math volcano.")
print("Leave explosives at the door. Identification please: ")
name = input()

#generate random, non-repeating list of integers from 0 to 10
rando = 0
prob_seq = []

for x in range (0, 10):
    rando = random.randint(0,10)
    #apply brute force
    for b in range (0, 100):
        if rando in prob_seq:
            rando = random.randint(0,10)
    prob_seq.append(rando)

correct = 0
lava_level = 0

#get user answers to equations
for x in range (0,9):
    #i am copy pasting instead of making up an extra variable?
    print_equation(lava_level, equation_strings, prob_seq, x)
    print("x = ")
    user_ans = input_function("int")
    while user_ans != answers[prob_seq[x]]:
        print("incorrect! try again: ")
        print_equation(lava_level, equation_strings, prob_seq, x)
        user_ans = input_function("int")
    if user_ans == answers[prob_seq[x]]:
        print("correct! "+name+" has found the correct value of x = "+str(answers[prob_seq[x]])+". lava level increases by "+str(100*(prob_seq[x]+10))+" feet")
        correct += 1
        lava_level += (100*(prob_seq[x]+10))

print(name+" solved "+str(correct)+" out of 10 equations correctly!\n"+name+"'s lava level is "+str(lava_level)+" feet\n")
if lava_level >= 10000:
    print(name+" floats away on an exhilarating deluge of lava")
elif lava_level >= 5000:
    print(name+" gets lost in the cavern. luckily, they brought explosives")
elif lava_level >= 0:
    print(name+" manages to escape, unsmitten by the volcano gods")
else:
    print(name+" is pulled down toward the center of the earth in a vortex of lava")

