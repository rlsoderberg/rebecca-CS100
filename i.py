#this thing isn't even working!!! aaaaaaaaa

def str_input_function():
    x = input("please enter a non-empty string variable: ")
    if not x:
        raise ValueError('empty string')
    return x

def str_empty_input_function():
    x = input("please press any key: ")
    return x  

def int_input_function():
    valid = False
    while valid == False:
        try:
            x = input("please enter an int variable: ")
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

def float_input_function():
    valid = False
    while valid == False:
        try:
            x = input("please enter a float variable: ")
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

def float_input_function():
    valid = False
    while valid == False:
        try:
            x = input("please enter a variable: ")
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

def input_function(type_name):
    if type_name == "str":
        input = str_input_function()
    if type_name == "str_empty":
        input = str_empty_input_function()
    elif type_name == "int":
        input = int_input_function()
    elif type_name == "float":
        input = float_input_function()
    else:
        input = str_input_function()
    return input

