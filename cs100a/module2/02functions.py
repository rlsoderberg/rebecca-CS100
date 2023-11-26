#import calendar module for month
import calendar

#6.

#number input function
def numberinput():
    #request user input for number
    valid = False
    while valid == False:
        try:
            number = int(input('what number would you like to use?'))
            if number == "":
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print('invalid input!')
    return number

def choiceinput(number):
    #request user to choose numbersum or factorial
    valid = False
    while valid == False:
        try:
            choice = int(input(f'would you like to find: \n1)the sum of numbers from 0 to {number}\n2)the product of numbers from 1 to {number}?'))
            if choice == "":
                raise ValueError('empty input')
            elif choice <1 or choice >2:
            #for some reason it liked it better when i used <> instead of !=
                raise ValueError('input out of range')
            valid = True
        except ValueError:
            print('invalid input')
    return choice

#number summing function
def numbersum(number):
    #initialize sum
    sum = 0

    #loop that sums numbers from 1 to a number
    for n in range(0, number):
        sum = sum + n

    return sum

#factorial function
def factorializer(number):
    #initialize factorial
    factorial = 1

    #loop that multiplies numbers from 1 to a number
    for n in range(1, number):
        factorial = factorial * n

    return factorial

#main function
def main():
    #get user input
    num = numberinput()
    choice = choiceinput(num)

    #pick one of the number functions, based on user choice
    if choice == 1:
        result = numbersum(num)
    elif choice == 2:
        result = factorializer(num)

    #list of function names
    functionlist = [0, 'number sum', 'factorial']

    #print results
    print(f'you chose to find the {functionlist[choice]} of {num}. the {functionlist[choice]} of {num} is {result}.')

#execute main
main()

#7.
#string input function
def getinput():
    #request string from user
    inputstring = input('please input a string: ')
    return inputstring

#find sum of numerical characters function
def sumstring(inputstring, sum):

    #loop through digits; check if current character is digit; if digit, add to sum
    for c in inputstring:
        if c.isdigit():
        #oh!!! i forgot the parentheses again!!! that totally messed me up!!!
            sum = sum + int(c)

    return sum

#result display function
def printresult(sumstring):
    #print result
    print(f'the sum of numerical characters in your string was {sumstring}.')

#main function
def main():
    inputstring = getinput()

    #initialize sum
    sum = 0

    sum = sumstring(inputstring, sum)
    printresult(sum)

main()

#8.

#input function
def getnum():
    #initialize number
    num = 0 

    #i stole this limiting method from my earlier version of this problem
    #it's neat, see, i can't help feeling like my brain is becoming more boring right now
    while num < 1 or num > 12:
        num = int(input('please enter a number from 1 to 12: '))

    return num

#so i used this one from my earlier version of this, and it looks the same to me!!
#define number to month function
def getmonth(number):
    month = calendar.month_name[number]
    return month

#display results function
def displayresults(num, month):
    print(f'{month} is the month corresponding to your number, {num}.')

def main():
    num = getnum()
    month = getmonth(num)
    displayresults(num, month)

main()

    



    