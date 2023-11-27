#7

#request for user to input a string
string = input("please enter a string (it's more fun if it contains numbers): ")

#initialize digit total
total = 0

#for loop of characters in string
for char in string:
    if char.isdigit():
        #do not forget to make the digit into an int, before adding it to the total
        total += int(char)

#display total of digits in string
print(f"total of digits in string '{string}' is {total}.")