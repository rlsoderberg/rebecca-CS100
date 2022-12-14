#input functions
import sys
sys.path.append("C:..\..")
from i import *
#here's the stuff for i input
type = "str"
blanky = 1

answer = main(type, blanky)
while (answer != "capybara"):
    if answer in list:        
        import incorrect
        incorrect.drawstuff(answer)
        #still can't handle 2 incorrects
        print("that is incorrect")
        print("what is your favorite animal?")
        answer = main(type, blanky)
    if answer not in list:
        print("that is incorrect")
        print("what is your favorite animal?")
        answer = main(type, blanky)
if answer == "capybara":
    print("that is correct")