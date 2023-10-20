#3

#initialize list
list = []

#initialize item
item = ''

#request for user to input items on grocery list
#right, i guess i should always start with input in a while loop like this
#because what if they start with none???
while item != 'none':
    item = input('enter a grocery item, or none to exit: ')
    #oh, haha, forgot to append items
    list.append(item)

#tell the user to go to the grocery store
print('now go to the grocery store')

#initialize cart item
cart_item = ''

#initialize done detector
done = 0

#no while loop here! user is mandated to complete shopping list!
while done == 0:
    cart_item = input('what did you put in your cart? ')
    if cart_item in list:
        list.remove(cart_item)
    if (len(list) - 1) == 0:
        print('you can check out now.')


