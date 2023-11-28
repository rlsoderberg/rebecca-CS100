import random

#create team list
team = []

#list of player numbers
numlist = [-2]
#i don't know why it seemed to want more numbers

# ask the user for names.
# enter 'done' when complete
player = ''
number = -1
while player != 'done':
    player = input('give me a player name: ')
    if player != 'done':
        number = random.randrange(99)
        team.append((str(player), str(number)))
#well... i'm going back to a version that works
#it didn't like me preventing duplicates!!!

sorted_by_num = sorted(team, key=lambda tup: tup[1])

print('your team is:')
#right, so i was trying to figure out why it was complaining about me 'subscripting' p
#so i was like, well, why don't i do for p in team?
#and then it's like oh yeah, i wanted something that was reversable
#so idk if the loop is the issue, or my lambda, or my tuple declaration, but those are my 3 suspects 
for p in range(0, len(sorted_by_num)):
    print(p[0] + p[1])

print('your team is:')
for p in reversed(range(0, len(sorted_by_num))):
    print(p[0] + p[1])
        
"""
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
        number = random.randrange(99)
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


print('your team is:')
for p in reversed(range(0, len(sorted_by_num))):
    print('\t' + p)
"""









