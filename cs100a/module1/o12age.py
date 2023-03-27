#request user input
age = float(input("How old are you? "))

valid = False
while valid == False:
    try:
        #print all matching responses
        if age >= 0 and age < 16:
            print("You can't do much yet.")
        if age >= 16:
            print("You can drive.")
        if age >= 18:
            print("You can vote.")
        if age >= 21:
            print("You can enjoy a beer.")
        if age >= 55:
            print("You get the senior discount.")
        valid = True
    except age < 0:
        print("Invalid age. Try again.")

