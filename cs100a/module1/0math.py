#so many files!!!
#i won't TOTALLY restart, but i'll go over everything to make sure i remember it
#and this had better be the last time, since i'm labeling it 0...

#so here... we have the input function.
#since we don't know how to... uh... reach over for the file things???
#i seemed to be using an int only input function last time. 
#since this is "math", right???
def int_input_function():
    valid = False
    while valid == False:
        try:
            x = int(input())
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

import random

#we are importing random so that we can randomize the problem sequence
#oh right, i just looked, and this is the one where i got way overly elaborate with the math volcano
#i'm going to try to get through pretty fast, so that i can conserve my precious bodily fluids

#i'm stealing the equation strings, and the answers, but i will type at least one so i remember how
equation_strings = ["5x + 3 = 13", "14 - 3x = 2", "9 - 2x = 3", "8x + 2 = 50", "2x + 16 = 40", 
                    "12 - 2x = 2", "7 = 49 - 6x", "30 + 7x = 86", "4x + 20 = 56", "3x - 3 = 39"]
answers = [2, 4, 3, 6, 12, 5, 7, 8, 9, 14]
#right, i was thinking of coming up with a way to auto solve these
#might be kind of pointless??? i'm going more for the web stuff right now

#quick narration
print("You are climbing a mountain, and you find a door behind a rock.")

opendoor = "a"

#handy dandy "while valid" loop!!!
valid = False
while valid == False:
    try:
        valid2 = False
        while valid2 == False:
            opendoor = str(input("Will you enter the door? Press Y to enter. Press N to climb away."))
            if opendoor in ("Y", "N"):
                valid2 = True
            else:
                print("Invalid input. Please enter Y or N: ")
        valid = True
    except:
        print("Invalid input. Please enter Y or N: ")

#look, it started complaining about invalid syntax!!! what did i do!!! i commented out most of my code!!!
#i did change that last loop a little. was that it?????

"""
#i do like the multiline comments in python

#i had to put this next part outside. I guess that makes sense, right?
#Not writing the entire program inside a giant loop? 
#Anyway, this is kind of a pointless question, but oh well, here it is anyway.
if opendoor == "Y":
    print("You have successfully opened the door!")
elif opendoor == "N":
    print("You have successfully climbed away. You keep finding doors, and you decide to go into one.")

key = input("Press any key to continue")

name = str(input("You enter a passage of semitranslucent indigo stone. \nA robotic voice buzzes from the walls: STATE YOUR NAME. You say: "))

#initilaizing random sequence, and array of randos
rando = 0
prob_seq = []

#generating prob_seq
for x in range (0,10):
    rando = random.randrange(0, 9)
    while rando in prob_seq:
        rando = random.randrange(0, 9)
    prob_seq.append(rando)

#initializing correct answers and... particle count?
correct = 0
particle_count = 0

#10 problems
for x in range (0, 9):
    print("CALCULATION " + x + "REQUIRED OF " + name)
    print(str(equation_strings[x]))
    user_ans = int_input_function()
    if user_ans == answers[prob_seq[x]]:
        correct += 1
        particle_count = (int(correct) + 1000) / rando*33
        print(particle_count + "particles deflected")
    elif user_ans != answers[prob_seq[x]]:
        particle_count = -1 * ((int(correct) + 1000) / rando*33)
        print(particle_count + "particles deflected")
        print("You feel the particles passing through your body")

"""






