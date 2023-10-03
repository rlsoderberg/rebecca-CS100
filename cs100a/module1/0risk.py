#well, it all looks fine
#not nearly as messy as math was
#can i skip this one??? i ran the old program and checked on its functionality
#troop counts can be confusing
#fine, i'll fix that really fast
#well, if i was rewriting this today, i'd also put more in functions

def troop_input(territory_name):
    valid = False
    while valid == False:
        try:
            valid2 = False
            while valid2 == False:
                print("\n")
                print("How many troops are on ",territory_name,"?")
                troops = int(input_function("int"))
                if troops >= 2:
                    valid2 = True
                else:
                    print("Invalid input. Please enter an integer 2 or higher.")
            valid = True        
        except ValueError:
            print("Invalid input. Please enter an integer 2 or higher.")
    return troops

#well... the dice rolls are so particular i don't know if it's worth defining this function?
#oh well, i'll go ahead and use variables
def num_dice_input(territory_name, troops, player_roll):
    valid = False
    while valid == False:
        try:
            valid2 = False
            while valid2 == False:
                numdice = int(input())
                if numdice == player_roll[0] or numdice == player_roll[1]:
                    if numdice <= troops:
                        valid2 = True
                    else:
                        print("You don't have that many troops! Please enter an integer less than " + str(troops))
                else:
                    print("Please enter an integer from " + str(player_roll[0]) + " to "  + str(player_roll[1]) + ".")
            valid = True        
        except ValueError:
            print("Please enter an integer from " + str(player_roll[0]) + " to "  + str(player_roll[1]) + ".")
    return numdice

import random

player_1_roll = [2,3]
player_2_roll = [1,2]

#oh look, here it is, reaching over...
import sys
sys.path.append('../..')

from i import input_function

#print introduction
print("\n  Welcome to \n• ROBOT RISK •\n")
print("Two territories are battling in a game of Risk.\n")
input("Press any key to continue.\n")

#request territory names
territory1=input("Enter the name of the attacking territory: ")
territory2=input("Enter the name of the defending territory: ")

#request number of troops on territory, limiting for more than 2

troops1 = troop_input(territory1)
troops2 = troop_input(territory2)


#initiate roll counter, turn counter, and dice counter
roll1 = []
roll2 = []

turncount = 1

numdice1 = 0
numdice2 = 0

print("\n")
print("Press any key to start Turn ",turncount,".")
input()

#turn loop until one player runs out of troops
while troops1 >= 2 and troops2 >= 1:

    #DON'T FORGET TO CLEAR ROLLS AT THE BEGINNING OF EACH ROUND!!!!!
    roll1.clear()
    roll2.clear()

    #print information for player 1
    print("\n")
    print(territory1, ": You have ",troops1," available troops.")

    print("How many dice (" + str(player_1_roll[0]) + " - " + str(player_1_roll[1]) + ") will " + str(territory1) + " roll to attack " + str(territory2) + "?")   
    numdice1 = num_dice_input(territory1, troops1, player_1_roll)

    #generate random rolls for player 1 according to number of dice
    if numdice1 == 3:
        for s in range (0,3):
            roll1.append(random.randint(1,6))
    elif numdice1 == 2:
        for s in range (0,2):
            roll1.append(random.randint(1,6))
    elif numdice1 == 1:
        for s in range (0,1):
            roll1.append(random.randint(1,6))

    #print information for player 2
    print("\n")
    print(territory2, ": You have ",troops2," available troops.")
    print(territory1," is attacking with ",numdice1," dice.")

    print("How many dice (" + str(player_2_roll[0]) + " - " + str(player_2_roll[1]) + ") will " + str(territory2) + " roll to defend " + str(territory2) + "?")   
    numdice1 = num_dice_input(territory2, troops2, player_2_roll)

    #generate random rolls for player 2 according to number of dice           
    if numdice2 == 2:
        for s in range (0,2):
            roll2.append(random.randint(1,6))
    elif numdice2 == 1:
        for s in range (0,1):
            roll2.append(random.randint(1,6))    




    #sort rolls in ascending order
    roll1.sort()
    roll2.sort()

    #find highest and second-highest rolls
    max1 = roll1[-1]
    max2 = roll2[-1]

    submax1 = roll1[-2]
    #check for roll array length to prevent array error
    if len(roll2) >= 2:
        submax2 = roll2[-2]
    else:
        submax2 = 0

    #display roll arrays
    print("\nPlayer 1 roll: ",roll1,"\nPlayer 2 roll: ", roll2)

    #display troop losses
    if max1 > max2 and submax1 > submax2:
        #limit troop losses according to number of dice
        if numdice2 >= 2:
            print(territory2," loses 2 troops.")
            troops2 -= 2
        else:
            print(territory2," loses 1 troops.")
            troops2 -= 1
    elif max1 > max2 and submax2 >= submax1:
        if numdice2 >= 2:
            print(territory1," loses 1 troops, and ",territory2," loses 1 troops.")
            troops1 -= 1
            troops2 -= 1
        else:
            print(territory2," loses 1 troops.")
            troops2 -= 1
    elif max2 >= max1 and submax1 > submax2:
        if numdice2 >= 2:
            print(territory1," loses 1 troops, and ",territory2," loses 1 troops.")
            troops1 -= 1
            troops2 -= 1
        else:
            print("Player 1 loses 1 troops.")
            troops1 -= 1
    elif max2 >= max1 and submax2 >= submax1:
            print(territory1," loses 2 troops.")
            troops1 -= 2


    #prepare turn counter and roll arrays for next turn
    turncount += 1
    roll1.clear()
    roll2.clear()

    print("\n")
    print("Press any key to start turn ",turncount,".")
    input()



#print results for end of game
print("Attack over! \n")
print(territory1," has ",troops1," troops and ",territory2," has ",troops2,"troops.\n")
if troops1>troops2:
    print(territory1," takes occupation of ",territory2," with ",troops1," troops.")
elif troops1<=troops2:
    print("Territory ownership remains unchanged.")
print("\n")
