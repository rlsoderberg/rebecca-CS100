#sorting out tuples and junk is way too complicated!!! let me try this again...
"""
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
            itemprop.append(propnames[c])
            print(propnames[c])
            if c == 1:
                itemprop.append(intputio())
            else:
                itemprop.append(inputio())
            itemprop.append("&&")
        tupleprop = tuple(itemprop)
        itemlist.append(tupleprop)
        itemprop.clear()

note = open("groceries.txt", 'w')
for c in itemlist:
    note.write(' '.join(str(s) for s in c) + '\n')
note.close()

propnames = ["Name of item: ", "Price of item (numbers only): ", "Quantity of item: "]

note = open("groceries.txt", 'r')
lineno = 1
for line in note:
    words = line.split()
    for wordnum in range(0, 3):
        print(propnames[wordnum])
        for n in words:
            try:
                print(words[n])
            except words[n] == "&&":
                wordnum += 1
    lineno = lineno + 1
note.close()
"""

def inputio():
    valid = False
    while valid == False:
        try:
            x =  input()
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

itemlist = []

item = ""
while item != "none":
    print("Input next grocery item, or type none to exit: ")
    item = inputio()
    if item != "none":
        itemlist.append(item)

note = open("groceries.txt", 'w')
lineno = 1
for c in itemlist:
    note.write(c+"\n")
    lineno = lineno + 1
note.close()

note = open("groceries.txt", 'r')
lineno = 1
for line in note:
    print(str(lineno) + ". " + line.strip())
    lineno = lineno + 1
note.close()