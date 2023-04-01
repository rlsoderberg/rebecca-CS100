import sys
sys.path.append('../..')

from i import input_function

grocery_list = []
item = ""

while item != "none":
    item = input("enter an item on your grocery list, or none to exit: ")
    if item != "none":
        grocery_list.append(item)

print("now go to the grocery store")

receipt = []
while len(grocery_list) > 0:
    print("items on grocery list: "+str(grocery_list))
    item = input("what item did you put in your cart? ")
    if item in grocery_list:
        print("how much does the "+item+" cost? ")
        cost = input_function("float")
        print("how many "+item+" did you put in your cart? ")
        qty = input_function("int")
        receipt.append((item, float(cost), int(qty)))
        grocery_list.remove(item)
    else:
        print('you strayed from the list. I hope you got Oreos')
print("you can check out now.")
total = 0.0

for lineitem in receipt:
    (item, cost, qty) = lineitem
    total = total + (cost*qty)
    print(str(qty) + " " + item + ": $" + str(format(cost, '.2f')) + " = " + str(format(cost*qty, '.2f')))
print("==================================")
print("TOTAL: $" + str(total))



