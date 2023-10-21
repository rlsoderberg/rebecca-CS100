#3

#initialize list
list = []

#initialize item
item = ''

#begin list input with exit term, just in case they exit right away
while item != 'none':
    item = input('enter a grocery item, or none to exit: ')
    list.append(item)

#tell the user to go to the grocery store
print('now go to the grocery store')

#initialize cart item
cart_item = ''

#initialize done detector
done = 0

#user must put all items from shopping list in cart, before they can check out
while done == 0:
    cart_item = input('what did you put in your cart? ')
    if cart_item in list:
        list.remove(cart_item)
    if (len(list) - 1) == 0:
        print('you can check out now.')


