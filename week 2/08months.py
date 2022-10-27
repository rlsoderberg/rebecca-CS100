months = ["Month Zero", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def getmonths(x):
    return months[x]

usermonth =  int(input("What number is the month? "))
print("Month ",usermonth, " is ",getmonths(usermonth))
