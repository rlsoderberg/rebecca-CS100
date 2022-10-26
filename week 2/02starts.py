#request user input
link = input("Enter a link: ")
if link.startswith("http"):
    valid = True
else:
    link = input("Invalid input. Enter a valid link: ")
print("Thank you for the valid link!")
