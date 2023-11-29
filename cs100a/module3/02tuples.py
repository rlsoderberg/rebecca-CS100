#oh never mind, i think i just panicked because i forgot where i was asking about item characteristics

#i am going to put #3 from 01lists here, because #4 and #5 continue it

#3. (from 01lists)

#our itemsforplan list, which is squishy
itemsforplan = []
#our itemsforcart, which is also squishy
itemsforcart = []
#do we really need that many squishy lists? here is the final list, which is unsquishy
itemsforcheckout = []

#initialize item
listitem = ''

#loop to get items on list until user is finished
while listitem != "none":
    #request user to input grocery item
    listitem = input("enter a grocery item, or none to exit: ")
    itemsforplan.append(listitem)
    #this seems overly complicated! #i swear, i had a simpler version of this that was working before...
    if listitem == "none":
        itemsforplan.pop(len(itemsforplan) - 1)

#make copy of list
itemsforcart = itemsforplan.copy()
print('now go to the grocery store')

#loop until list is empty and cart is full
while len(itemsforcart) > 0:
    #string is simple, string is free
    itemname = input('what did you put in your cart? ')
    #a whole try except for itemprice
    valid = False
    while valid == False:
        try:
            itemprice = float(input(f'how much did the {itemname} cost? '))
            if itemprice == '':
                raise ValueError('empty input')
            valid = True
        except ValueError:
            print('invalid input')
    #and all that again for itemquantity
    valid = False
    while valid == False:
        try:
            itemquantity = int(input(f'what is the quantity of {itemname}? '))
            if itemquantity == '':
                raise ValueError('empty input')
            valid = True
        except ValueError:
            print('invalid input')
    #put the 3 item characteristics in a tuple. double parentheses to the rescue!!!
    cartitem = ((itemname, itemprice, itemquantity))

    #append cartitem to itemsforcheckout
    itemsforcheckout.append(cartitem)

    #remember to remove item from cart
    if itemname in itemsforcart:
        itemsforcart.remove(itemname)

#print receipt
print('you can check out now.')
print("here's your receipt: ")

#initialize total cost
totalcost = 0

#loop to go through items
#whoa, look at this! unpacking the tuple in the for loop!
for (name, price, quantity) in itemsforcheckout:
    #i am taking heavily from example down here, and it is sooo good!
    print(f'\t{name} @ ${price:.2f} X {quantity} = {price*quantity:.2f}')
    totalcost = totalcost + (quantity*price)
print('---------------------------------------------')
print(f'total: ${totalcost:.2f}')

#format total cost
#but yeah, i guess this is what got me out of sorts
#this isn't exactly working the way i want it to!!!
roundcost = '%.2f' % totalcost
print(f'Total Cost: {totalcost}')

#4 get price/quantity when putting item in cart (see cart loop, 'while len(glist) > 0:')

#5 print receipt, total cost