import random

#create team list
team = []

#list of player numbers
numlist = [0, 0, 0, 0]
#i don't know why it seemed to want more numbers

#print instructions
print("please enter names of team members; type 'done' when done.")
#request name input for each player
player = ''
while player != 'done':
    player = input('give me a player name: ')
    #you know what, i don't understand why this 'if player != done' is here!!! i'm going to try it without!!!
    #i tried putting it back in, and it did NOT help with my mystery error...
    number = -1
    while number not in numlist:
        #it keeps getting stuck on this!!!!!!!
        number = random.randrange(1, 99)
    #appending tuple to list requires two parentheses
    team.append((player, number))

#oh, here's lambda again!
#i swear, when i first used it for math tutor in lesson 1, i saw it in the preview for the next week
#but we never went over it!!
#now lambda is something i really SHOULD ask about
#because look, here i am once again stealing it from some person on the internet
sorted_by_num = sorted(team, key=lambda tup: tup[1])

print('your team is:')
for p in range(0, len(sorted_by_num)):
    print('\t' + p)

"""
print('your team is:')
for p in reversed(range(0, len(sorted_by_num))):
    print('\t' + p)
"""









