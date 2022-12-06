#input functions
import sys
sys.path.append("C:..\..")
from i import *
import turtle

type = "str"
blanky = 1
print("what is your favorite animal?")
answer = main(type, blanky)

list = ["cat", "dog", "bird", "fish"]


while answer != "capybara":
    if answer in list:         
        import incorrect
        incorrect.drawstuff(answer)
        turtle.bye()
        print("Incorrect, try again.")
        print("What is your favorite animal?")
        answer = main(type, blanky)
    elif answer == "capybara":
            print("that is correct")
    else:
        print("Incorrect, try again.")
        print("What is your favorite animal?")
        answer = main(type, blanky)
    



