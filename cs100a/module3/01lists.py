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
while name != 'done':
    name = input('name of player 1: ')
    if name != 'done':
        number = random.randrange(99)
        while number in numlist:
            number = random.randrange(99) 
        #ah, perhaps the key is to make the tuple first, and then append that
        #(name, number) = player
        #oh hey wait, that's UNPACKING a tuple. how are you supposed to create them???
        #well, it's true that, in this final version, at no point do i use the double parentheses
        #let me try those...
        player = ((name, number))
        team.append(player)

#sort by numbers
sorted_by_num = sorted(team, key=lambda tup: tup[1])

print('your team is:')
print(sorted_by_num)

#sort by numbers in reverse
reverse = sorted(team, key=lambda tup: -tup[1])

print('your team in reverse:')
print(reverse)

#2. (continuation)

#see if user name is in list of names
if name in team:
    print("I can't wait to play")
else:
    print("Put me in coach, I'm ready to play.")

#3 (relocated to 02tuples.py, where it is joined with #4 and #5)









