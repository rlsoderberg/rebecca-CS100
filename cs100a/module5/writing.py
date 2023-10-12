#well, right, since i'm trying to make this function, i might just copy and paste? sry sys

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
            total = price*quantity
            item = (item_name, price, quantity, total)
            grocery_list.append(item)

    return grocery_list

#grocery list confirmation is reinvogorated by file import combo
grocery_list = create_list()

#see, i should check if the file exists, and then create it if it doesn't, but you know what???
#i will try to learn without getting too distracted. how about that???
#oh wait, w automatically does that? srsly what am i doing?
#ohhhh, it wanted the filename in quotes. oooomg

grandtotal = 0.0
f = open ("grocery.txt", 'w')
f.write("GROCERY LIST\n")
for tuple in grocery_list:
    (n, p, q, t) = tuple
    price = ("%.2f" % p) 
    total = ("%.2f" % t)
    f.write(f"{q}x {n} at ${price} each: ${total}\n")
    grandtotal += float(total)

f.write(f"Your grand total is ${grandtotal}")
print("YOUR GROCERY LIST HAS BEEN WRITTEN")

#really, i need to go through and make a list of stuff to remember, since i forget everything
#i'll work on it!!!!!!!!!!!!!

f.close()



