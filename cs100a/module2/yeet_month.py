#8

#import calendar
import calendar

#define number to month function
def getmonth(number):
    month = calendar.month_name[number]
    return month

#define int input function
def int_input_function():
    valid = False
    while valid == False:
        try:
            number = int(input())
            if number == "":
                raise ValueError('empty input')
            valid = True
        except ValueError:
            print('Invalid Input')
    return number

#request for user to input a number from 1 to 12
print('please enter a number from 1 to 12:')

number = int_input_function()

#repeat request until user enters number from 1 to 12
while number <= 0 or number > 12:
    number = int_input_function()

#get month
month = getmonth(number)

#print month
print(f'the month corresponding to your number, {number}, is {month}.')
    