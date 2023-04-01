def int_input_function():
    valid = False
    while valid == False:
        try:
            x = int(input())
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
            x = float(input())
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x   

def input_function(type_name):
    if type_name == "int":
        input = int_input_function()
    elif type_name == "float":
        input = float_input_function()
    return input

