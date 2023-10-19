#1

#create team list
team = []

#oh, forgot to initialize name!
name = ''

#here i am coming up from the bottom, and i'd better introduce myself, along with the program...
print("hi, i'm becca, and i'm here to take down the team roster.")

#while loop to take input until user presses 'x' to exit
while name != 'x':
    #request for user to input player name
    name = input('enter player name, or enter x to exit: ')
    #great thing about this input is there's no errors, haha love it

    #add new player name to list
    team.append(name)

#introduce the team print loop
print('now printing team, from name most recently entered, back to name first entered')

"""#well, i had to google how to go backwards in a for loop. apparently it involves -1???
#oh bother, range will be the death of me!!! needed to take away extra for 'x'
#and i had to do it down to -1 because range is so weird! come on!!!
for x in range(len(team)-2, -1, -1):
    print(team[x])"""

#now i'm rewriting it in sorted order
#what do you mean, 'what order is sorted'???
#i'm just going back to starting from first entered
#unless we're categorizing the players by some other quality?
#you know i don't know how to do that yet...
for x in range(0, len(team)-1):
    print(team[x])

#right, this is legal for same file, because it's part of the same program!!

#2

if 'becca' in team or 'BECCA' in team or 'Becca' in team:
    print("I can't wait to play")
else:
    print("Put me in coach, I'm ready to play.")