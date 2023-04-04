import calendar

#fancy double input function requests int variable, as an operand or as a month
def input_function(purpose):
    valid = False
    while valid == False:
        try:
            if purpose == "calc":
                x = int(input("enter an integer to calculate: "))
            elif purpose == "month":
                x = int(input("enter an integer from 1 to 12 to find the corresponding month: "))
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            if purpose == "calc":
                print("nonempty int values only")
            elif purpose == "month":
                print("integers between 1 and 12 only")
    return x 
#digit total function sums all the digits
def digit_total(string):
    total = 0
    for s in string:
        if s.isnumeric():
            total += int(s)
    return total



quit = ""
while quit != "q":

    problem = ""
    quit = ""
    print("which problem would you like to view? 1. factorial calculations, 2.sum of digits in string, or 3. getmonth?")
    while problem != "1" and problem != "2" and problem !="3":
        problem = input()

    if problem == "1":
        print("would you like to view: \n1. sum of all digits from 1 to n (nth triangular number) \n2. product of all digits from 1 to n (factorial)")
        subproblem = ""
        while subproblem != "1" and subproblem !="2":
            subproblem = input()
        if subproblem == "1":
            n = int(input_function("calc"))
            tringnum = (n*(n+1))/2
            print("nth triangular number of "+str(n)+" is "+str(tringnum))
        if subproblem == "2":
            n = int(input_function("calc"))
            factorial = 1
            for b in range (1, n+1):
                factorial = b * factorial
            print("factorial of "+str(n)+" is "+str(factorial))

    elif problem == "2":
        string = input("please enter string to find its digit total:")
        digit_total = digit_total(string)
        print("digit total for '"+string+"' is "+str(digit_total))

    elif problem == "3":
        month_number = int(input_function("month"))
        month = calendar.month_name[month_number]
        print("month "+str(month_number)+" is "+month)

    while quit != "q" and quit != "m":
        quit = input("press q to quit or m to return to problem menu: ")






