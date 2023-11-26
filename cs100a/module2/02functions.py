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

    
    