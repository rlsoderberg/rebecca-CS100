#making list
grocery_list = []
#initializing item
#this is totally the wrong way to do it, but otherwise it was complaining about it!!!
item=[0, 1, 2]
item_name=""
#add items to list (except none)
while item_name != "none":
    item_name = input("enter a grocery item, or none to exit: ")
    if item_name!= "none":
        #oh, my types inputs aren't safe from breakage, are they?
        item[0] = item_name
        price = float(input(f"How much does the {item_name} cost? "))
        item[1] = price
        quantity = int(input(f"How many {item_name} are you buying? "))
        item[2] = quantity
    grocery_list.append(item)
#i was trying to remove none, idk, how to i reference a tuple with a specific name?

print("here's your grocery list:")
print(grocery_list)
#for some reason it just printed eggs 3 times!!!! 


#remove items from list if they are bought... until none remain
print("now go to the grocery store")
while len(grocery_list) > 0:
    item = input("what did you put in your cart?")
    if item in grocery_list:
        grocery_list.remove(item)


    

