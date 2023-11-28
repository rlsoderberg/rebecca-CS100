import random

#1.

#ask for user's name
name = input("hi! you must be my new basketball coaching assistant! what's your name? ")
print("first you're going to fill out our team roster.")

 
# #create team list
team = []

#list of player numbers
numlist = []

# ask the user for names.
# enter 'done' when complete
player = ''
number = -1
while player != 'done':
    player = input('name of player 1: ')
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
#now, according to the tuple lesson, the key to creating a tuple is to put the parentheses first

#sort by numbers
sorted_by_num = sorted(tupleteam, key=lambda tup: tup[1])

print('your team is:')
print(sorted_by_num)

#sort by numbers in reverse
reverse = sorted(tupleteam, key=lambda tup: -tup[1])

print('your team in reverse:')
print(reverse)

#2. (continuation)

#see if user name is in list of names
if name in tupleteam:
    print("I can't wait to play")
else:
    print("Put me in coach, I'm ready to play.")

#3 (relocated to 02tuples.py, where it is joined with #4 and #5)









