#input function requests int variable, and rejects empty strings, in the voice of a polite string problem deployment machine
def input_function():
    valid = False
    while valid == False:
        try:
            x = int(input("please enter an int variable: "))
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x 

quit = "0"
#we play until we quit
while quit == "0":
    print("STRING PROBLEMS\npress 1 for problem 1, 2 for problem 2, or 3 for problem 3")
    problem = "0"
    while problem != "1" and problem != "2" and problem != "3":
        problem = input()
#built in python string methods
    if problem == "1":
        user_string = input("please enter a string: ")
        print("would you like to see your string in 1. uppercase   2. lowercase   3. title case ?")
        case = input_function()
        if case == "1":
            print(str(user_string.upper()))
        elif case == "2":
            print(user_string.lower())
        elif case == "3":
            print(user_string.title())
#startswith method
    elif problem == "2":
        link = input("enter a website link: ")
        if link.startswith("http"):
            print("thank you for the valid link")
        elif not link.startswith("http"):
            print("that's not a nice link!")
#strip method          
    elif problem == "3":
        name = input("please enter your name: ")
        print("hello, "+name.strip()+". thank you for stripping for me")

    print("press q to quit and m to return to problem menu")
    while quit != "q" and quit != "m":
        quit = input()
    
