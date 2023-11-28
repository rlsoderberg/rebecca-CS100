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