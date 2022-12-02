#import random module for rock paper scissors
import random

#array for play names
plays = ["Rock", "Paper", "Scissors"]
#request user input
user = int(input("Choose a number: 1. Rock, 2. Paper, or 3. Scissors? "))

#generate computer's play
computer = random.randrange(1,3)

#display results
print("\n")
print("You have chosen ",plays[user - 1],".")
print("Computer has chosen ",plays[computer - 1],".")
print("\n")
print("User: ",plays[user - 1],"/",user," vs. Computer: ",plays[computer - 1],"/",computer)

if user > computer:
    print(user," > ",computer,"! User wins!")
elif computer > user:
    print(user," < ",computer,"! Computer wins!")
elif user == computer:
    print(user," = ",computer,"! Tie!")