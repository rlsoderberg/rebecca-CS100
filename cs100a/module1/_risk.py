#importing input function
import sys
sys.path.append("../..")

from i import int_input_function, input_function

import random

def num_dice_input(troops):
    numdice = 0
    while numdice != 3 and numdice != 2:
        try:
            numdice = int(input("How many dice will you roll? "))
            if not numdice:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return numdice  

player_1_roll = [2,3]
player_2_roll = [1,2]

#print introduction
print("\n  Welcome to \n• ROBOT RISK •\n")
print("Two territories are battling in a game of Risk.\n")
input("Press any key to continue.\n")

#request territory names
print("Enter the name of the attacking territory: ")
territory1=input_function()
print("Enter the name of the defending territory: ")
territory2=input_function()

#request number of troops on territory, limiting for more than 2

print(f"How many troops are on {territory1}?")
troops1 = int_input_function()
print(f"How many troops are on {territory2}?")
troops2 = int_input_function()


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
    print(f"There are {troops1} troops on {territory1} and {troops2} troops on {territory2}.")
    print(f"You can roll between {player_1_roll[0]} and {player_1_roll[1]} dice to attack {territory2}.")
    numdice1 = num_dice_input(troops1)

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
    print(f"{territory1} ({troops1} troops) is attacking {territory2} ({troops2} troops). It is attacking with {numdice1} dice.")
    print(f"You can roll between {player_2_roll[0]} and {player_2_roll[1]} dice to defend {territory2} against {territory1}.")


    #i keep getting a number for numdice1 that equals the total number of troops on the territory???

    numdice2 = num_dice_input(troops2)

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
print("\n\n\nAttack over! \n")
print(territory1," has ",troops1," troops and ",territory2," has ",troops2,"troops.\n")
if troops1>troops2:
    print(territory1," takes occupation of ",territory2," with ",troops1," troops.")
elif troops1<=troops2:
    print("Territory ownership remains unchanged.")
print("\n")
