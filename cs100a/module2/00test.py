import calendar

#input function
def getnum():
    num = input('please enter a number from 1 to 12: ')
    return num

#convert number to month function
def numtomonth(num):
    month = calendar.month_name[num]

#display results function
def displayresults(num, month):
    print(f'{month} is the month corresponding to your number, {num}.')

def main():
    num = getnum()
    month = numtomonth(num)
    displayresults(num, month)

main()