#input functions
import sys
sys.path.append("C:..\..")
from i import *

type = "str"
blanky = 1
print("what is your favorite animal?")
answer = main(type, blanky)

list = ["cat", "dog", "bird", "fish"]

while (answer not in list) and (answer != "capybara"):
    print("incorrect, try again")
    answer = main(type, blanky)
if answer in list:         
    import incorrect
    incorrect.drawstuff(answer)
elif answer == "capybara":
        print("that is correct")

