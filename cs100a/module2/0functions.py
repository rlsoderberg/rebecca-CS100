#import input function
import sys
sys.path.append('../..')

print("Would you like to:\n1) Calculate the month corresponding to an integer?\n2) Calculate the sum of the integer's digits\n3) Calculate the integer's factorial\nWhich will it be?")

#well... i'm just going to make a custom input function?
valid = False
while valid == False:
    try:
        problem_choice = int(input("Please enter 1, 2, or 3: "))
        if problem_choice not in range (0, 4):
            raise ValueError("out of range")
        else:
            valid = True
    except ValueError:
        print("Invalid Input!")