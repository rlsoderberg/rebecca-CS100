#import calendar 
import calendar

filename = input('what file do you want to write my shoveling schedule to? ')
#open text file
f = open(filename, 'w')
#i am practicing writing to a file from a for loop because last time it felt kind of weird?
for x in range(0, 7):
    f.write(f'shovel the walk on {calendar.day_name[x]}\n')
#close text file
f.close()
print('it has been written.')
print(f"now let's read the contents of {filename}:\n")
f = open(filename, "r")
#i used this, because my original wasn't working
for line in f:
    print(line.strip())
#oh i see!!! the key is using f(the opened file) instead of filename(the name of the file)
"""
for line in filename:
    print(line)
"""
f.close()

#grocery list program
itemsforplan = []
#simplified version with no items for cart, no items for checkout, and no tuples

#initialize item
listitem = ''

#loop to get items on list until user is finished
while listitem != "none":
    #request user to input grocery item
    listitem = input("enter a grocery item, or none to exit: ")
    itemsforplan.append(listitem)
    #this seems overly complicated! #i swear, i had a simpler version of this that was working before...
    if listitem == "none":
        itemsforplan.pop(len(itemsforplan) - 1)

print("writing your shopping list to grocery.txt")

#initialize total cost
totalcost = 0

#open grocery file for writing
file = open('grocery.txt', 'w')
#loop to go through items
#whoa, look at this! unpacking the tuple in the for loop!
for name in itemsforplan:
    #i am taking heavily from example down here, and it is sooo good!
    file.write(f'\n{name}')
file.close()

#open grocery file for reading
file = open('grocery.txt', 'r')

#now it's giving me just 'g' for this!! what did i do??
#oh, i uh... wasn't really utilizing the read method???
for line in file:
    #i am now using readline to read line by line
    print(file.readline())
    delete = input('do you want to remove this item from the list? ')


