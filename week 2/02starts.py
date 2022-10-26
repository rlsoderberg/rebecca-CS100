from operator import truediv


link = input("Enter a link: ")
valid = False
while valid == False:
    if link.startswith("http"):
        valid = True
    else:
        link = input("Invalid input. Enter a valid link: ")
print("Thank you for the valid link!")
