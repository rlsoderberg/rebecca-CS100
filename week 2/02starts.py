#input functions
def inputio():
    valid = False
    while valid == False:
        try:
            link = input("Enter a link: ")
            valid = True
        except ValueError:
            print("Invalid Input!")
    return link

def input2():
    x = inputio()
    while x == "":
        print("I didn't hear you!")
        x = inputio()
    return x

#check if valid
link = input2()
if link.startswith("http"):
    valid = True
else:
    while not link.startswith("http"):
        link = input("Invalid input. Enter a valid link: ")
#thank user 
print("Thank you for the valid link!")
