#input function
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

list = []

item = ""
while item != "none":
    print("Enter a grocery item, or none to exit: ")
    item = inputio()
    if item != "none":
        list.append(item)
        print("You put ",item,"in your cart.")

print("You make your way to the checkout line...")
#i'm using this again
ellipse = ["..."]

from time import sleep
import sys

for s in range(0,3):          
    for c in ellipse:          
        print(c, end='')    
        sleep(0.5)          
    print('')   

print("Oh no! You have a shopping cart accident!")
sleep(0.5)
print("Now all your grocery items are mixed up...")
import random
#for some reason shuffle wasn't working, so i made a new list
randolist = random.sample(list, len(list))
print("Press enter to check out.")
enter = input()

for c in randolist:
    print("You check out ",c,".")
    sleep(0.5)

print("Hopefully that's everything!")


