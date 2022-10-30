def inputio():
    valid = False
    while valid == False:
        try:
            x =  input()
            while x == "":
                print("Out of range!")
                x = input()
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

#the teams
reverseteam = []
unreverseteam = []

#the players
print("List players on team, from longest time played on team, to shortest.")
print("Enter 'done' when you're finished.")

player = ""
while player != "done":
    print("Give me a player name: ")
    player = inputio()
    if player != "done":
        reverseteam.insert(0, player)
        unreverseteam.append(player)

print("Team members from newest to oldest are: \n", reverseteam)
print("Team members from oldest to newest are: \n", unreverseteam)

print("\n \n")
print("What's my name?")
username = inputio()
print("Let me see if I'm on the team...")

#i totally stole this from somewhere!!!! i do like creating suspense
ellipse = ["..."]

from time import sleep
import sys

for s in range(0,3):          
    for c in ellipse:          
        print(c, end='')    
        sleep(0.5)          
    print('')      

if username in reverseteam:
    print("Looks like I am on the team!")
    print("I can't wait to play.") 
else:
    print("I'm not on the team yet!")
    print("Put me in coach, I'm ready to play.")

