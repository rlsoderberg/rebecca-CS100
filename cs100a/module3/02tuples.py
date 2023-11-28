#i am going to put #3 from 01lists here, because #4 and #5 continue it

#3. (from 01lists)

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
    #string is simple, string is free
    itemname = input('what did you put in your cart? ')
    #a whole try except for itemprice
    valid = False
    while valid == False:
        try:
            itemprice = float(input('how much did the item cost?'))
            if itemprice == '':
                raise ValueError('empty input')
        except ValueError:
            print('invalid input')
    #and all that again for itemquantity
    valid = False
    while valid == False:
        try:
            itemquantity = float(input('how much did the item cost?'))
            if itemprice == '':
                raise ValueError('empty input')
        except ValueError:
            print('invalid input')
    #put the 3 item characteristics in a tuple
    
    #i just wasted a bunch of mental energy because i added this to 01lists but i forgot to add it to 00tests!
    #remember, the goal is always 0
    if tocart in glist:
        glist.remove(tocart)

print('you can check out now.')
print("here's your receipt: ")
print

#4 get price/quantity when putting item in cart (see cart loop, 'while len(glist) > 0:')