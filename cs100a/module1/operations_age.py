#define int input function
def int_input_function():
    valid = False
    while valid == False:
        try: 
            result = int(input())
            #'if not result' malfunctioned with 0, so i prefer this
            if result == '':
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print('Invalid Input')
    return result

#request integers
print('please give me two intergers.')
print('integer one:')
int1 = int_input_function()
print('integer two:')
int2 = int_input_function()
print('and, by the way, how old are you? (whole years only please)')
age = int_input_function()

#identify operation
print('\noperation 1: addition')
print('int1 + int2 =')
print(f'that is, {int1} + {int2} = \n')
#calculate answer 
sum = int1 + int2

#press any key!!! just plain old input
input('press any key to see the solution')

#using f string for string interpolation and formatting
print(f'solution: {int1} + {int2} = {sum}')
#press any key
input('press any key to see the next operation')

#skipped to division

#identify operation
print('\noperation 2: division')
print('int1 / int2')
print(f'that is, {int1} / {int2} = \n')
#press any key
print('press any key to see the solution')
input()
#special case if int2 = 0
#try-except with ZeroDivisionError
valid = False
while valid == False:
    try:
        quotient = int1/int2
        print(f'solution: {int1} / {int2} = {quotient}')
        valid = True
    except ZeroDivisionError:
        print("int 2 = 0, and we cannot divide by zero")
        print(f'solution: {int1} / {int2} = undefined')
        valid = True

#NUMBER 12 (prisoner reference, in hindsight)
#output suitable activities for user, based on age input
#we already asked for age up at the top

#introduce the age display
print(f"now, let's see what we can calculate based on your age of {age} years...")
if age < 0:
    print('invalid age')
if age >= 16:
    print('you can drive')
if age >= 18:
    print('you can vote')
if age >= 21:
    print('you can enjoy a beer')
if age >= 55:
    print('you get the senior discount')





