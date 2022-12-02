#input functions
#how do i do this??????????????????????????????????????????????
#if, for example, i put in 99&enter, and then enter, i break it!!!!!!!!!!!!!
#how do i make it so the different parts connect with each other??????????
#and how do i make it so i have an input function that is as versatile as possible????????
def inputio():
    valid = False
    while valid == False:
        try:
            x =  int(input())
            while x < 0 or x > 11:
                while x == "":
                    print("Out of range!")
                print("Out of range!")
                x = int(input())
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

#create list of months
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def getmonths(x):
    return months[x-1]
    
#request user input and display results
print("What number is the month? ")
usermonth = inputio()
print("Month ",usermonth, " is ",getmonths(usermonth))
