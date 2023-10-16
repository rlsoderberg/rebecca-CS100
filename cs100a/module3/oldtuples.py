#input functions
import sys
sys.path.append("../..")

from i import int_input_function, float_input_function

def create_list():
    #making list
    grocery_list = []
    #initializing item
    #add items to list (except none)
    item_name = ""
    #i had to put grocery_list.append(item) under if item_name != none!!!!
    while item_name != "none":
        item_name = input("enter a grocery item, or none to exit: ")
        if item_name!= "none":
            print(f"How much does the {item_name} cost? ")
            price = float_input_function()
            print(f"How many {item_name} are you buying? ")
            quantity = int_input_function()
            item = (item_name, price, quantity)
            grocery_list.append(item)

    print("YOUR GROCERY LIST:")
    #oh, this weird little thing, %.2f! like, what is that???
    for item in grocery_list:
        (n, p, q) = item
        price = ("%.2f" % p)
        print(f"{q}x {n} at ${price} each: {quantity*p}")
    #ohhhh, you have to copy lists!!!
    full_grocery_list = grocery_list.copy()
    return grocery_list

grocery_list = create_list()

#remove items from list if they are bought... until none remain
print("now go to the grocery store")
while len(grocery_list) > 0:
    item_name = input("what did you put in your cart? ")
    for item in grocery_list:
        (n, p, q) = item
        if n == item_name:
            grocery_list.remove(item)

#print receipt
print("YOUR RECEIPT:")
for item in grocery_list:
    (n, p, q) = item
    price = ("%.2f" % p)
    print(f"{q}x {n} at ${price} each")


    

