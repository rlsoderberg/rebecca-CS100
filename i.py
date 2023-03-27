def str_input_function(type_name):
    valid = False
    while valid == False:
        try:
            x = input("give me a "+str(type_name)+": ")
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

def int_input_function(type_name):
    valid = False
    while valid == False:
        try:
            x = input("give me a "+str(type_name)+": ")
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

def float_input_function(type_name):
    valid = False
    while valid == False:
        try:
            x = input("give me a "+str(type_name)+": ")
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

def input_function(type_name):
    x = type_name
    if x == "str":
        input =  str_input_function(str)
    elif x == "int":
        input =  int_input_function(int)
    elif x == "float":
        input =  float_input_function(float)



#yeah, this is not the most efficient. you know what???