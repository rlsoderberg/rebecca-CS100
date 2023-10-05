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

    print("\n\n\n\n\nWould you like to:\n1) Calculate the month corresponding to an integer?\n2) Calculate the sum of the integer's digits\n3) Calculate the integer's factorial\n\nWhich will it be?\n")

    #wait, this is an easy way to do it
    problem_choice = 0

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
        print("Month "+str(month_number)+" is "+month_name)

    elif (problem_choice == 2):

        string = input("Please enter any integer string to find its digit total: ")
        digit_total = digit_total(string)
        print("Digit total for '"+string+"' is "+str(digit_total))

    elif (problem_choice == 3):

        n = int(input("Please enter any integer to calculate factorial: "))
        factorial = 1
        for b in range (1, n+1):
            factorial = b * factorial
        print("Factorial of "+str(n)+" is "+str(factorial) + "\n")

    print("Press (almost) any key to return to main menu, or press x to exit")
    exit = input()

