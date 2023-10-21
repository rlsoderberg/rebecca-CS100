#initialize list
list = []

#initialize item
item = ''

#initialize item_name
item_name = ''

#while loop, allowing user to exit anytime
while item_name != 'none':
    #request for user to input grocery item, as well as price and quantity
    item_name = input('enter a grocery item, or none to exit: ')
    if item_name != 'none':
        item_price = input(f'how much does {item_name} cost?') 
        item_quantity = input(f'what quantity of {item_name} do you need?')
        #store item characteristics in tuple
        item = (item_name, item_price, item_quantity)
        #store tuple in list
        list.append(item)


#programmer's note... so far, things to look out for
#1. variable names
#2. parentheses
#3. indentation


#create a copy of the full list. remember to put parentheses behind copy, a behavior
full_list = list.copy()

#tell the user to go to the grocery store
print('now go to the grocery store')

#initialize cart item
cart_item = ''

#initialize done detector
done = 0


#user must put all items from shopping list in cart before they can check out
while len(list) > 0:
    #request 
    cart_item = input('what did you put in your cart? ')
    for item in list:
        #unpack tuple item from list
        (n, p, q) = item
        #use item name to check if list item is same as item in cart; if so, remove item from list
        if n == cart_item:
            list.remove(item)

#introduce checkout
print('you can check out now.')

#5

#press any key. build suspense for receipt.
input('press any key to complete checkout.')
print("here's your receipt:")

#loop printing items bought from shopping list
for x in full_list:
    #unpacking tuple from list copy
    (name, price, quantity) = x
    print(f"{name}  price: ${price}  quanitity: {quantity}")



