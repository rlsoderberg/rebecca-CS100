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

def print_equation(lava_level, equation, x):
    print("\ncurrent lava level: "+str(lava_level)+" feet")
    print("equation "+str(x+1))
    print(str(equation))

#equations and correct answers
equation_tuple = [("5x + 3 = 13", 2, ""), ("14 - 3x = 2", 4, ""), ("9 - 2x = 3", 3, ""), ("8x + 2 = 50", 6, ""), ("2x + 16 = 40", 12, ""), ("12 - 2x = 2", 5, ""), ("7 = 49 - 6x", 7, ""), ("30 + 7x = 86", 8, ""), ("4x + 20 = 56", 9, ""), ("3x - 3 = 39", 14, "")]

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

n = 0
#i think most of the problem here is i don't REALLY understand how to use tuples
for e in equation_tuple:
    (equation, answer, user_ans) = e
    print_equation(lava_level, equation, x)
    print("x = ")
    user_ans = input_function("int")
    while user_ans != answer:
        print("incorrect! try again: ")
        lava_level -= (100*(prob_seq[n]+10))
        print("\ncurrent lava level: "+str(lava_level)+" feet")
        print("equation "+str(x+1))
        print(str(equation))
        print("x = ")
        user_ans = input_function("int")
    if user_ans == answer:
        print("correct! "+name+" has found the correct value of x = "+str(answer)+". lava level increases by "+str(100*(prob_seq[n]+10))+" feet")
        correct += 1
        lava_level += (100*(prob_seq[n]+10))
        x += 1
        n += 1

print(name+" solved "+str(correct)+" out of 10 equations correctly!\n"+name+"'s lava level is "+str(lava_level)+" feet\n")
if lava_level >= 10000:
    print(name+" floats away on an exhilarating deluge of lava")
elif lava_level >= 5000:
    (name+" gets lost in the cavern. luckily, they brought explosives")
elif lava_level >= 0:
    print(name+" manages to escape, unsmitten by the volcano gods")
else:
    print(name+" is pulled down toward the center of the earth in a vortex of lava")

