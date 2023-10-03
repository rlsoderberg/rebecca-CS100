#import calendar
import calendar

#import input function
import sys
sys.path.append('../..')

def digit_total(string):
    total = 0
    for s in string:
        if s.isnumeric():
            total += int(s)
    return total


exit = "0"
while exit != "x":
    
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

    if (problem_choice == 1):

        month_number = 0

        valid = False
        while valid == False:
            try:
                month_number = int(input("Please enter an integer from 1 to 12: "))
                if month_number not in range (0, 13):
                    raise ValueError("out of range")
                else:
                    valid = True
            except ValueError:
                print("Invalid Input!")
        month_name = calendar.month_name[month_number]
        print("month "+str(month_number)+" is "+month_name)

    elif (problem_choice == 2):

        string = input("please enter integer string to find its digit total: ")
        digit_total = digit_total(string)
        print("digit total for '"+string+"' is "+str(digit_total))

    elif (problem_choice == 3):

        n = int(input("please enter integer to calculate factorial: "))
        factorial = 1
        for b in range (1, n+1):
            factorial = b * factorial
        print("factorial of "+str(n)+" is "+str(factorial))

exit = input("press (almost) any key to return to main menu, or press x to exit")