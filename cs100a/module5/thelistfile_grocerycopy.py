#initialize list
list = []

#initialize item
item = ''

#initialize item_name
item_name = ''

#open grocery file for writing list
g = open('grocery.txt', 'w')

while item_name != 'none':
    item_name = input('enter a grocery item, or none to exit: ')
    if item_name != 'none':
        item_price = input(f'how much does {item_name} cost?') 
        item_quantity = input(f'what quantity of {item_name} do you need?')
        #the difference with writing to a file, is instead of using a tuple, you print directly into the file
        #remember to include enter at the end, if you are making a list
        g.write(item_name + ' price: $' + item_price + ' quantity: ' + item_quantity + '\n')
        #remember, you still need to use the list, for putting items in the cart
        list.append(item_name)

#don't forget to close the file!
g.close()


#programmer's note... so far, things to look out for
#1. variable names
#2. parentheses
#3. indentation


#writing to file eliminates need for list copy
#full_list = list.copy()

#tell the user to go to the grocery store
print('now go to the grocery store/n')

#initialize cart item
cart_item = ''

#initialize done detector
done = 0

#user must put all items from shopping list in cart before they can check out
while len(list) > 0:
    #request 
    cart_item = input('what did you put in your cart? ')
    for item_name in list:
        if item_name == cart_item:
            list.remove(item_name)

#introduce checkout
print('you can check out now.')

#5

#press any key. build suspense for receipt.
input('press any key to complete checkout.')
print("here's your receipt:")

#open file again for reading
g = open('grocery.txt', 'r')

#initialize lineno for text file
lineno = 1

#for each line, print line number and line from file
for line in g:
    print(str(lineno) + '. ' + line)
    lineno += 1

#don't forget to close the file!
g.close()



