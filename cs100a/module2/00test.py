import calendar

#input function
def getnum():
    #initialize number
    num = 0 

    #i stole this limiting method from my earlier version of this problem
    #it's neat, see, i can't help feeling like my brain is becoming more boring right now
    while num <= 0 or num > 12:
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