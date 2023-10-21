#1

#create team list
team = []

#initialize name
name = ''

#introduce self as roster taker (roster taker later becomes involved), along with the program
print("hi, i'm rebecca, and i'm here to take down the team roster.")

#while loop to take input until user presses 'x' to exit
while name != 'x':
    #request for user to input player name
    name = input('enter player name, or enter x to exit: ')
    #add new player name to list
    team.append(name)

#introduce the team print loop
print('now printing team, from name most recently entered, back to name first entered')

for x in range(len(team)-2, -1, -1):
    print(team[x])


#2

#print whether roster taker is on list, and roster taker's response
if 'rebecca' in team or 'REBECCA' in team or 'Reecca' in team:
    print("I can't wait to play")
else:
    print("Put me in coach, I'm ready to play.")