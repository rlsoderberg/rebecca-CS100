#input functions
def inputio():
    valid = False
    while valid == False:
        try:
            usermonth =  int(input("What number is the month? "))
            valid = True
        except ValueError:
            print("Invalid Input!")
    return usermonth

def input2():
    x = inputio()
    while x == "":
        print("I didn't hear you!")
        x = inputio()
    return x

#create list of months
months = ["Month Zero", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def getmonths(x):
    return months[x]
    
#request user input and display results
usermonth = input2()
print("Month ",usermonth, " is ",getmonths(usermonth))
