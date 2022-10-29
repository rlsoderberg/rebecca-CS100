#input functions
#how do i do this??????????????????????????????????????????????
#if, for example, i put in 99&enter, and then enter, i break it!!!!!!!!!!!!!
#how do i make it so the different parts connect with each other??????????
#and how do i make it so i have an input function that is as versatile as possible????????
def inputio():
    valid = False
    while valid == False:
        try:
            x =  int(input("What number is the month? "))
            valid = True
        except ValueError:
            print("Invalid Input!")
    while x == "":
        print("I didn't hear you!")
        x = int(input("What number is the month? "))
    while x < 0 or x > 11:
        print("Out of range!")
        x = int(input("What number is the month?"))
    return x

#create list of months
months = ["Month Zero", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def getmonths(x):
    return months[x]
    
#request user input and display results
usermonth = inputio()
print("Month ",usermonth, " is ",getmonths(usermonth))
