#input functions
def inputio():
    valid = False
    while valid == False:
        try:
            user = int(input())
            valid = True
        except ValueError:
            print("Invalid input! Choose a number: 1. Rock, 2. Paper, or 3. Scissors? ")
    return user

def input2():
    user = inputio()
    while user == "":
        print("I didn't hear you!")
        user = inputio()
    return user
    
def input3():
    user = input2()
    #why did i have to write this out??? had while user < 0 or user > 3
    while user != 1 and user != 2 and user != 3:
        print("Invalid input! Choose a number: 1. Rock, 2. Paper, or 3. Scissors? ")
        user = int(input())
    return user

#import random module for rock paper scissors
import random

#array for play names
plays = ["0", "Rock", "Paper", "Scissors"]

#win counters
compwin = 0
userwin = 0

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
    user = input3()
    #actual rock paper scissors!!!
    if computer == 1:
        if user == 1:
            win = 0
        elif user == 2:
            userwin+=1
            win = 1
        elif user == 3:
            compwin+=1
            win = 2
    elif computer == 2:
        if user == 1:
            compwin+=1
            win = 2
        elif user == 2:
            win = 0
        elif user == 3:
            userwin+=1
            win = 1
    elif computer == 3:
        if user == 1:
            userwin+=1
            win = 1
        elif user == 2:
            compwin+=1
            win = 2
        elif user == 3:
            win = 0


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

