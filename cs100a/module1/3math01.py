#hey, i was going to copy the examples more this 3rd time around. where are the examples??? am i tripping???
#WHY DO I GET THE FEELING THAT I KEEP NOT SEEING THE EXAMPLES AAAAAA
#also this folder is going to get ginormous oops


#i'm just putting an input function up here???

def input_function():
    valid = False
    while valid == False:
        try:
            x = int(input("please enter the int value of x = "))
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

import random

#equations and correct answers
equation_strings = ["5x + 3 = 13", "14 - 3x = 2", "9 - 2x = 3", "8x + 2 = 50", "2x + 16 = 40", "12 - 2x = 2", "7 = 49 - 6x", "30 + 7x = 86", "4x + 20 = 56", "3x - 3 = 39"]
#i should totally come up with a way to auto solve these
answers = [2, 4, 3, 6, 12, 5, 7, 8, 9, 14]

#didn't make enough sense!!!
print("You are climbing a mountain. Suddenly, your hand slips.")
print("There seems to be a slippery patch on the side of the mountain.")

valid = False
while valid == False:
    try:
        brushaside = input("Press a to avoid the slippery patch, or b to brush aside dirt from the slippery patch.") 
        valid = True     
    #hey!!!!! this isn't working!!!! omg soooo much to fix
    except brushaside != "a" and brushaside != "b":
        print("Invalid input. Please enter a or b.")

if brushaside == "a":
    print("You try to avoid the slippery patch, but it seems to be part of a large, smooth area.")
elif brushaside == "b":
    print("You brush aside the dirt, and you find a large, smooth area.")

#what a mess! i'll have to delay these, too
print("You uncover what seems to be a doorway in the mountain.")
print("The door begins to vibrate, and a loud, metallic voice begins to speak in monotone.")

print("WELCOME TO THE MATH VOLCANO.")
print("A drawer slides out of the mountain, beside the doorway")

print("TAKE 1 INFLATABLE LAVA BOAT.")
print("An inflatable lava boat? You quizzically inspect the shrivelled, oblong shape in the drawer.")

#look, it's getting late, i'll fix more in the morning. sheesh!! this is going to take forever!!!
takeboat = str(input("Press b to take the boat, or a to throw your explosives and run."))
name = input("LEAVE EXPLOSIVES AT THE DOOR. Identification please: ")

#generate random, non-repeating list of integers from 0 to 10
rando = 0
prob_seq = []

for x in range (0, 10):
    rando = random.randint(0,9)
    #apply brute force. is this really what i should be doing??? can't i go bring back some better search function??
    for b in range (0, 100):
        if rando in prob_seq:
            rando = random.randint(0,10)
    prob_seq.append(rando)

correct = 0
lava_level = 0

#did i seriously write 'for x in range (0, 10):'???
for x in range (0,9):
    #added a little welcome to make beginning less abrupt
    if (x == 0):
        print("\nwelcome, "+name)
    print("current lava level: "+str(lava_level)+" feet")
    print("equation "+str(x+1))
    #wait, what the heck? i thought changing it to (0, 9) would fix it, but it's still messing up here
    print(str(equation_strings[prob_seq[x]]))
    user_ans = input_function()
    if user_ans == answers[prob_seq[x]]:
        print("correct! "+name+" has found the correct value of x = "+str(answers[prob_seq[x]])+". lava level increases by "+str(100*(prob_seq[x]+10))+" feet")
        correct += 1
        lava_level += (100*(prob_seq[x]+10))
    elif user_ans != answers[prob_seq[x]]:
        print("incorrect! "+name+" has not found the correct value of x = "+str(answers[prob_seq[x]])+". lava level decreases by "+str(50*(prob_seq[x]+10))+" feet")
        lava_level -= (50*(prob_seq[x]+10))

print(name+" solved "+str(correct)+" out of 10 equations correctly!\n "+name+"'s lava level is "+str(lava_level)+" feet\n")
#i think i didn't put enough zeroes
if lava_level >= 10000:
    print(name+" floats away on an exhilarating deluge of lava")
elif lava_level >= 1000:
    #this one didn't quite make sense
    print(name+" paddles through the cavern on their lava boat, and gets lost. luckily, they brought explosives")
elif lava_level >= 0:
    print(name+" manages to escape, unsmitten by the volcano gods")
else:
    print(name+" is pulled down toward the center of the earth in a vortex of lava")

#is there no cthulhu easter egg in here?


