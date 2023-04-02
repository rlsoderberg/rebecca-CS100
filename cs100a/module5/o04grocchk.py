#input function
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
#prompt input
item = ""
while item != "none":
    print("Input next grocery item, or type none to exit: ")
    item = inputio()
    if item != "none":
        itemlist.append(item)

#write to note
note = open("groceries.txt", 'w')
for c in itemlist:
    note.write(c+"\n")
note.close()

#print numbers + lines
note = open("groceries.txt", 'r')
lineno = 1
for line in note:
    print(str(lineno) + ". " + line.strip())
    lineno = lineno + 1
note.close()