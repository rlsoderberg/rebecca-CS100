##input functions
def inputio():
    valid = False
    while valid == False:
        try:
            x =  input()
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

def intputio():
    valid = False
    while valid == False:
        try:
            x =  float(input())
            while x < 0:
                while x == "":
                    print("Out of range!")
                print("Out of range!")
                x = int(input())
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

itemlist = []
propnames = ["Name of item: ", "Price of item (numbers only): ", "Quantity of item: "]
itemprop = []

item = ""
while item != "none":
    print("Press enter for new grocery item, or type none to exit: ")
    item = inputio()
    if item != "none":
        for c in range (3):
            print(propnames[c])
            if c == 1:
                itemprop.append(intputio())
            else:
                itemprop.append(inputio())
        tupleprop = tuple(itemprop)
        itemlist.append(tupleprop)
        itemprop.clear()

print("You make your way to the checkout line...")
input("Press enter to check out.")

print("Items checked out: ")

total = 0
for c in itemlist:
    print(c[0])
    print("Price: ",c[1])
    print("Quantity: ",c[2])

    try:
        total = (total + c[1])
    except ValueError:
        pass
print("Total Cost: ",total)


