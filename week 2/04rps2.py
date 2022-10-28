#import random module for rock paper scissors
import random

#array for play names
plays = ["0", "Rock", "Paper", "Scissors"]

#input arrays
def inputio():
    valid = False
    while valid == False:
        try:
            x = int(input())
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

def input2():
    x = inputio()
    while x == "":
        print("I didn't hear you!")
        x = inputio()
    return x

#repeat match cycle until someone wins
print("\n")
print("Rock Paper Scissors Tournament: Best of Seven \n")
win = 0
while win == 0:
    #request user input
    print("Choose a number: 1. Rock, 2. Paper, or 3. Scissors?")
    #generate computer's play
    computer = random.randrange(1,3)
    #check for invalid input
    valid = False
    while valid == False:
        try:
            valid2 = False
            while valid2 == False:
                user = input2()
                if user > 0 and user < 4:
                    valid2 = True
                    #actual rock paper scissors!!!
                    if computer == 1:
                        if user == 1:
                            win = 0
                        elif user == 2:
                            win = 1
                        elif user == 3:
                            win = 2
                    elif computer == 2:
                        if user == 1:
                            win = 2
                        elif user == 2:
                            win = 0
                        elif user == 3:
                            win = 1
                    elif computer == 3:
                        if user == 1:
                            win = 1
                        elif user == 2:
                            win = 2
                        elif user == 3:
                            win = 0
                else:
                    print("Invalid input! Choose a number: 1. Rock, 2. Paper, or 3. Scissors? ")
            valid = True
        except ValueError:
            print("Invalid input! Choose a number: 1. Rock, 2. Paper, or 3. Scissors? ")
    #display match results
    print("\n")
    print("You chose ",user,plays[user])
    print("Computer chose ",computer,plays[computer], "\n")
    if win == 1:
        print("User wins!")
    elif win == 2:
        print("Computer wins!")
    elif win == 0:
        print("Tie! Play again.")



        
        

