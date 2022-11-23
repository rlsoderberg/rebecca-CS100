#input functions
def inputio():
    valid = False
    while valid == False:
        try:
            x =  int(input())
            while x < 1 or x > 3:
                while x == "":
                    print("Out of range!")
                print("Out of range!")
                x = int(input())
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

#import random module for rock paper scissors
import random

#array for play names
plays = ["0", "Rock", "Paper", "Scissors"]

#win counters
compwin = 0
userwin = 0

#repeat match cycle until computer or user gets 4 wins
print("\n")
print("Rock Paper Scissors Tournament: Best of Seven \n")
while compwin < 4 and userwin <4:
    #request user input
    print("Choose a number: 1. Rock, 2. Paper, or 3. Scissors?")
    #generate computer's play
    computer = random.randrange(1,3)
    #check for invalid input
    user = inputio()
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
        print("Tie!")
    
    #display win count
    print("User win count: ",userwin)
    print("Computer win count: ",compwin, "\n")
        
        
#display overall results
print("\n \n \n")
print("You got ",userwin," points.")
print("Computer got ",compwin,"points.")
print("\n")
print("User: ",userwin," vs. Computer: ",compwin)

if user > computer:
    print(userwin," > ",compwin,"! User wins!")
elif computer > user:
    print(userwin," < ",compwin,"! Computer wins!")

