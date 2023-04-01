import sys
sys.path.append('../..')

from i import input_function 

import random

#function to print data from equation tuple, as well as lava level, which we can't seem to get rid of
def print_equation(lava_level, equation, n):
    print("\ncurrent lava level: "+str(lava_level)+" feet")
    print("equation "+str(ordern))
    print(str(equation))

#equations and correct answers
equation_tuple = [("1", "5x + 3 = 13", 2, 0), ("2", "14 - 3x = 2", 4, 0), ("3", "9 - 2x = 3", 3, 0), ("4", "8x + 2 = 50", 6, 0), ("5", "2x + 16 = 40", 12, 0), ("6, ""12 - 2x = 2", 5, 0), ("7", "7 = 49 - 6x", 7, 0), ("8, ""30 + 7x = 86", 8, 0), ("9", "4x + 20 = 56", 9, 0), ("10, ""3x - 3 = 39", 14, 0)]
rand_equation_tuple = random.sample(equation_tuple, len(equation_tuple))

#request identification
print("Welcome to the math volcano.")
print("Leave explosives at the door. Identification please: ")
name = input()


correct = 0
lava_level = 0

#ummm, this sounds funny, but i was avoiding using random.sample to generate rand_probnum
#but it looks like that is the easiest way, when you're dealing with tuples
#i was just like, why is pete asking us to generate a non repeating randomized list
#if he doesn't secretly have a good way of doing it???
#still holding out for secret way of creating non repeating randomized lists
#i guess sample MIGHT be a good way for now
for e in rand_equation_tuple:
    (n, equation, answer, user_ans) = e
    ordern = 0
    print_equation(lava_level, equation, ordern)
    print("x = ")
    user_ans = input_function("int")
    while user_ans != answer:
        print("incorrect! try again: ")
        lava_level -= (100*(int(n)+10))
        print_equation(lava_level, equation, ordern)
        print("x = ")
        user_ans = input_function("int")
    if user_ans == answer:
        print("correct! "+name+" has found the correct value of x = "+str(answer)+". lava level increases by "+str(100*(int(n)+10))+" feet")
        correct += 1
        lava_level += (100*(int(n)+10))
        ordern += 1

print(name+" solved "+str(correct)+" out of 10 equations correctly!\n"+name+"'s lava level is "+str(lava_level)+" feet\n")
if lava_level >= 10000:
    print(name+" floats away on an exhilarating deluge of lava")
elif lava_level >= 5000:
    (name+" gets lost in the cavern. luckily, they brought explosives")
elif lava_level >= 0:
    print(name+" manages to escape, unsmitten by the volcano gods")
else:
    print(name+" is pulled down toward the center of the earth in a vortex of lava")

