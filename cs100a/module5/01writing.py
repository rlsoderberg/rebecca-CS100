print("what filename should i write to?")
filename = input()

#cleaning invalid characters
invalid = '<>:"/\|?* '

for char in invalid:
	filename = filename.replace(char, '')

#appending file extension to string
filename += '.txt'

f = open (filename, 'w')
f.write('listening to a thousand knives\n')
f.write('birds, knives, and insects\n')
f.write('holding on to something from before\n')
f.close()

import sys
sys.path.append('../..')

from i import input_function

#create grocery list, item variable
grocery_list = []
item = ""

#enter items for grocery list, until none are left
while item != "none":
    item = input("enter an item on your grocery list, or none to exit: ")
    if item != "none":
        grocery_list.append(item)

print("now go to the grocery store")

#receipt list
receipt = []
#get user input on which item to remove, until none are left in grocery list
while len(grocery_list) > 0:
    print("items on grocery list: "+str(grocery_list))
    item = input("what item did you put in your cart? ")
    if item in grocery_list:
        #request additional information for item tuple (don't forget proper types!!)
        print("how much does the "+item+" cost? ")
        cost = input_function("float")
        print("how many "+item+" did you put in your cart? ")
        qty = input_function("int")
        #put entire tuple into receipt list
        receipt.append((item, float(cost), int(qty)))
        grocery_list.remove(item)
    else:
        print('you strayed from the list. I hope you got Oreos')
print("you can check out now.")

total = 0.0

#lineitem tuple
f = open ("grocery_list.txt", 'w')
for lineitem in receipt:
    (item, cost, qty) = lineitem
    #calculate total, using cost and qty
    total = total + (cost*qty)
    #write price data to grocery list text file, and don't forget to newline
    f.write(str(qty) + " " + item + ": $" + str(format(cost, '.2f')) + " = " + str(format(cost*qty, '.2f'))+"\n")
f.write("==================================\n")
f.write("TOTAL: $" + str(total))
#and don't forget to close the file!!
f.close()



