import random

#create team list
team = []

#list of player numbers
numlist = []

# ask the user for names.
# enter 'done' when complete
player = ''
number = -1
while player != 'done':
    player = input('give me a player name: ')
    if player != 'done':
    #oh, it got stuck because it didn't like my 'while number not in numlist' loop!!!
        team.append(player)

#i'm going to try zip, to make a list of tuples, and make a whole other thing for the numbers
for p in team:
    number = random.randrange(99)
    while number in numlist:
        number = random.randrange(99)
    numlist.append(number)
    #well, this is simpler, which is a good sign
    #and it kind of looks like it's working
    
#zip up names with numbers
tupleteam = list(zip(team, numlist))

#sort by numbers
sorted_by_num = sorted(tupleteam, key=lambda tup: tup[1])

print('your team is:')
print(sorted_by_num)

#sort by numbers in reverse
reverse = sorted(tupleteam, key=lambda tup: -tup[1])

print('your team in reverse:')
print(reverse)

        











