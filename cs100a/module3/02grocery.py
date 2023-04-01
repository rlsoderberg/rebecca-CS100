grocery_list = []
item = ""

while item != "none":
    item = input("enter an item on your grocery list, or none to exit: ")
    if item != "none":
        grocery_list.append(item)

print("now go to the grocery store")
while len(grocery_list) > 0:
    print("items on grocery list: "+str(grocery_list))
    item = input("what item did you put in your cart? ")
    if item in grocery_list:
        grocery_list.remove(item)
    else:
        print('you strayed from the list. I hope you got Oreos')
print("you can check out now.")



