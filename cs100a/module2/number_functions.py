#6

#define functions for megasum and factorial
def megasum(number):
    total = 0
    addend = 1
    while addend <= number:
        total += addend
        addend += 1
    return total

def factorial(number):
    total = 1
    factor = 1
    while factor <= number:
        total *= factor
        factor += 1
    return total

#define int input function
def int_input_function():
    valid = False
    while valid == False:
        try:
            intput = int(input())
            if intput == '':
                raise ValueError('empty sring')
            valid = True
        except ValueError:
            print('Invalid Input.')
    return intput

#request for user to enter a number
print('please enter a number: ')
number = int_input_function()

#request for user to choose megasum or factorial
choice = input(f'would you like to a. calculate the megasum of {number} or b. calculate the factorial of {number}?')

#repeat choice request until user enters 'a' or 'b'
while choice != 'a' and choice != 'b':
    choice = input(f'would you like to a. calculate the megasum of {number} or b. calculate the factorial of {number}?')

#initialize total
total = 0

#run megasum or factorial function, depending on user input
if choice == 'a':
    total = megasum(number)
elif choice == 'b':
    total = factorial(number)

#print result of function
print(f'your result is {total}')








