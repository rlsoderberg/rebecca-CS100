#calendar for calculating months
import calendar

#import input function
import sys
sys.path.append('../..')

from i import int_input_function

#wait, what is happening over in afunctions.py???
#oh i see, i was doing multiple problems...
print("Welcome to the Integer Zone")
print("Would you like to:\n1) Calculate the month corresponding to an integer?\n2) Calculate the sum of the integer's digits\n3) Calculate the integer's factorial\nWhich will it be? 1, 2, or 3?")

problem_choice=0
valid = False
while valid == False:
        problem_choice = int_input_function
        if problem_choice == 1 or problem_choice == 2 or problem_choice == 3:
            valid = True
        else:
            print("Please enter 1, 2, or 3: ")


    
    



