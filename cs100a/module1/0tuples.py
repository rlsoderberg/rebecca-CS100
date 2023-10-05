#input functions
def int_input_function():
    valid = False
    while valid == False:
        try:
            x = int(input())
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

def float_input_function():
    valid = False
    while valid == False:
        try:
            x = float(input())
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  


#making list
grocery_list = []
#initializing item
item=[]
item_name=""
#add items to list (except none)
while item_name != "none":
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
#still adding item twice???????????? and like, it's doing multiples of a list for the whole shopping list?

print("here's your grocery list:")
print(grocery_list)


#remove items from list if they are bought... until none remain
print("now go to the grocery store")
while len(grocery_list) > 0:
    item_name = input("what did you put in your cart?")
    #really don't know how to do this!!!!!!!!!!!!!!
    if item_name in item in grocery_list:
        grocery_list.remove(item)
    print(grocery_list)



    

