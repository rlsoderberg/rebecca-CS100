#input functions
import sys
sys.path.append("..\..")

from i import int_input_function, float_input_function


#making list
grocery_list = []
#initializing item
#add items to list (except none)
item_name = ""
#PROBLEM WITH AUTOMATICALLY ADDING BLANK ITEM, AND DELETING ALL ITEMS
while item_name != "none":
    item=[]
    item_name = input("enter a grocery item, or none to exit: ")
    if item_name!= "none":
        item.append(item_name)
        print(f"How much does the {item_name} cost? ")
        price = float_input_function()
        item.append(price)
        print(f"How many {item_name} are you buying? ")
        quantity = int_input_function()
        item.append(quantity)
    grocery_list.append(item)

print("here's your grocery list:")
print(grocery_list)


#remove items from list if they are bought... until none remain
print("now go to the grocery store")
while len(grocery_list) > 0:
    item_name = input("what did you put in your cart?")
    if item_name in item in grocery_list:
        grocery_list.remove(item)
    print(grocery_list)



    

