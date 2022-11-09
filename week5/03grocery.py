#input functions
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

#i should totally put some propnames in here!!!
note = open("groceries.txt", 'w')
for c in itemlist:
    note.write(' '.join(str(s) for s in c) + '\n')