#calendar for calculating months
import calendar

#import input function
import sys
sys.path.append('../..')

from i import int_input_function

#wait, what is happening over in afunctions.py???
#oh i see, i was doing multiple problems...
print("Welcome to the Integer Zone")
print("Would you like to:\n1) Calculate the month corresponding to an integer?\n2) Calculate the sum of the integer's digits\n3) Calculate the integer's factorial\nWhich will it be?")

#well... i'm just going to make a custom input function?
#it's not working!!! whyyy 
#now... is there some way to this with a valid loop? hmmmm
valid = False
while valid == False:
    try:
        problem_choice = int(input("Please enter 1, 2, or 3: "))
        if problem_choice not in range (1, 3):
            raise ValueError("out of range")
        else:
            valid = True
    except ValueError:
        print("Invalid Input!")

print("SUCCESS!")
    
    