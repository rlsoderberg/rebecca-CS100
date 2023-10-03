#hey, i was going to copy the examples more this 3rd time around. where are the examples??? am i tripping???
#WHY DO I GET THE FEELING THAT I KEEP NOT SEEING THE EXAMPLES AAAAAA
#also this folder is going to get ginormous oops


#i'm just putting an input function up here???
def input_function():
    valid = False
    while valid == False:
        try:
            x = int(input("VALUE OF X: "))
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

import random

equation_strings = ["5x + 3 = 13", "14 - 3x = 2", "9 - 2x = 3", "8x + 2 = 50", "2x + 16 = 40", "12 - 2x = 2", "7 = 49 - 6x", "30 + 7x = 86", "4x + 20 = 56", "3x - 3 = 39"]
#i should totally come up with a way to auto solve these
#oooh, I don't know, I think I would have to use a library or something
answers = [2, 4, 3, 6, 12, 5, 7, 8, 9, 14]

#provide narration
print("You are climbing a mountain. Suddenly, your hand slips.")
print("There seems to be a slippery patch on the side of the mountain.")

#well, i finally copied an input function from risk, and apparently value error was what i wanted
valid = False
while valid == False:
    try:
        valid2 = False
        while valid2 == False:
            print("\n")
            brushaside = str(input("Press a to avoid the slippery patch, or b to brush aside dirt from the slippery patch."))
            if brushaside in ("a", "b"):
                valid2 = True
            else:
                print("Invalid input. Please enter a or b")
        valid = True        
    except ValueError:
        print("Invalid input. Please enter a or b.")


if brushaside == "a":
    print("\nYou try to avoid the slippery patch, but it seems to be part of a large, smooth area.")
elif brushaside == "b":
    print("\nYou brush aside the dirt, and you find a large, smooth area.")

print("You uncover what seems to be a doorway in the mountain.")
print("The doorway begins to vibrate, and a loud, metallic voice begins to speak in monotone.")
print("WELCOME TO THE MATH VOLCANO.")
key = input("Press any key to continue.")

print("\nA drawer slides out of the mountain, beside the doorway.")
print("TAKE 1 INFLATABLE LAVA BOAT.")
print("An inflatable lava boat? You look quizzically at the shrivelled, oblong shape in the drawer.")

valid = False
while valid == False:
    try:
        valid2 = False
        while valid2 == False:
            takeboat = str(input("Press a to throw your handy hiking explosives and run away, or b to take the boat."))
            if takeboat in ("a", "b"):
                valid2 = True
            else:
                print("Invalid input. Please enter a or b")
        valid = True        
    except ValueError:
        print("Invalid input. Please enter a or b.")

if takeboat == "a":
    print("\nYou run away, but the drawer follows you. \nAs soon as you finally take the boat, to see what happens, you are teleported to a cavern.")
elif takeboat == "b":
    print("\nYou take the boat, and you are teleported to a cavern.")

key = input("Press any key to continue.")

print("\nYou find yourself on a raised platform in the middle of a cavern. \nYou see lava below you, all around the platform.")
print("The metallic voice reverberates within the cavern.")
name = str(input("IDENTIFICATION PLEASE: "))

rando = 0
prob_seq = []
correct = 0


#isn't it weird that range doesn't include the last number, but randint does? is that what is happening
for x in range (0, 10):
    rando = random.randint(0,9)
    #what was the point of that brute force exactly??? look, idk how to deal with duplicates, kind of hard to test
    while rando in prob_seq:
        rando = random.randint(0,9)
    prob_seq.append(rando)

lava_level = 0

#ALL CAPS EVERYTHING. is that some clipping i hear oOoOoOoH
for x in range (0,10):
    if (x == 0):
        print("\nWELCOME, "+name.upper()+".")
        print("PLEASE INFLATE BOAT.")
        print("You see the lava beginning to rise to your level. You inflate the boat and sit down inside.")
    key = input("Press any key to continue.")
    print("\nCURRENT LAVA LEVEL: "+str(lava_level)+" FEET")
    print("\nEQUATION "+str(x+1)+" OF "+name.upper()+":")
    print(str(equation_strings[prob_seq[x]]))
    user_ans = input_function()
    if user_ans == answers[prob_seq[x]]:
        print("CORRECT! "+name.upper()+" HAS IDENTIFIED X = "+str(answers[prob_seq[x]])+". LAVA LEVEL INCREASES BY "+str(100*(prob_seq[x]+10))+" FEET.")
        correct += 1
        lava_level += (100*(prob_seq[x]+10))
    elif user_ans != answers[prob_seq[x]]:
        print("INCORRECT! "+name.upper()+" HAS NOT IDENTIFIED X = "+str(answers[prob_seq[x]])+". LAVA LEVEL DECREASES BY "+str(50*(prob_seq[x]+10))+" FEET.")
        lava_level -= (50*(prob_seq[x]+10))

print("\n"+name.upper()+" SOLVED "+str(correct)+" EQUATIONS CORRECTLY. \nLAVA LEVEL IS "+str(lava_level)+" FEET.")
key = input("Press any key to continue.\n")

if lava_level >= 10000:
    print("You are carried out the top of the mountain, and float down on an exhilarating deluge of lava.")
elif lava_level >= 1000:
    print("You paddle through the cavern on the lava boat, and get lost.")
    if takeboat == "a":
        print("You regret wasting your hiking explosives.")
        print("You eventually find a way out, with old fasioned spelunking, no explosives.")
    else:
        print("You are very thankful that you didn't waste your explosives.")
        print("You use the explosives to defend against feral cave bats, and you eventually find a way out.")

elif lava_level >= 0:
    print("You find yourself back in the vestibule of the volcano.")
    print("With all the lava at a uniform level, you just paddle around until you get teleported out.")
else:
    print("You are pulled down toward the center of the earth in a vortex of lava.")


