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

#3.

#grocery list
glist = []

#initialize item
item = ''

#loop to get items on list until user is finished
while item != "none":
    #request user to input grocery item
    item = input("enter a grocery item, or none to exit: ")
    glist.append(item)
    #this seems overly complicated! #i swear, i had a simpler version of this that was working before...
    if item == "none":
        glist.pop(len(glist) - 1)


print(glist)
print('now go to the grocery store')

#loop until list is empty and cart is full
while len(glist) > 0:
    tocart = input('what did you put in your cart? ')
    #i just wasted a bunch of mental energy because i added this to 01lists but i forgot to add it to 00tests!
    #remember, the goal is always 0
    if tocart in glist:
        glist.remove(tocart)

print('you can check out now.')












