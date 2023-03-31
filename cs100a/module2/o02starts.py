#input functions
#input functions
def inputio():
    valid = False
    while valid == False:
        try:
            x =  input()
            while x == "":
                print("Out of range!")
                x = input()
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

#check if valid
print("Enter a link: ")
link = inputio()
if link.startswith("http"):
    valid = True
else:
    while not link.startswith("http"):
        link = input("Invalid input. Enter a valid link: ")
#thank user 
print("Thank you for the valid link!")
