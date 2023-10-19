#4

#we are copying and pasting grocery, because... tuples??? who knows how this will go!!!

#initialize list
list = []

#initialize item
item = ''

#request for user to input items on grocery list
#right, i guess i should always start with input in a while loop like this
#because what if they start with none???

#now i need to initialize item_name, because i am using it for my while loop!
item_name = ''

while item_name != 'none':
    item_name = input('enter a grocery item, or none to exit: ')
    if item_name != 'none':
        item_price = input(f'how much does {item_name} cost?') #yoooo!!! there is room for illegal prices here!!!
        item_quantity = input(f'what quantity of {item_name} do you need?')
        item = (item_name, item_price, item_quantity)
        list.append(item)
#what, i really don't get it!!! why isn't it exiting???
#ohhh i get it i get it!!! i forgot to put item_name in the top of the while loop!!!!
#always make sure your variable names are correct!!!!!
#like, i need to make a list of things to check for
#1. variable names
#2. parentheses
#3. indentation


#create a copy of the full list
full_list = list.copy

#tell the user to go to the grocery store
print('now go to the grocery store')

#initialize cart item
cart_item = ''

#initialize done detector
done = 0


#no while loop here! user is mandated to complete shopping list!
#wait, what? there is indeed a while loop. with the wonderfully simple condition of len(list) > 0
while len(list) > 0:
    cart_item = input('what did you put in your cart? ')
    #oh i see, in oldtuples, i unpacked the tuple before removing the item from the list
    for item in list:
        (n, p, q) = item
        if n == cart_item:
            list.remove(item)

#well, that worked, unpacking first!

#now i am going to print this down here instead.
print('you can check out now.')

#5

#we are further modifying the program to display a receipt!

#press any key. build suspense for receipt.
input('press any key to complete checkout.')
print("here's your receipt:")

#look, it's mad here, and i don't get it!!!
#what, does it want me to use parentheses because it's a list of tuples?
#it didn't make me do that before!!!
#oh right, i just noticed the receipt isn't working on oldtuples!!!

for x in full_list():
    (name, price, quantity) = x
    print(f"{name}  price: ${price}  quanitity: {quantity}")

#so it's possibly a problem with making a copy of the list, and possibly a problem with printing receipt?
#ask about that, and range???

