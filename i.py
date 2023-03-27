#look at all this copy pasting!!! can i do, like, varying criteria or something somehow???
def blankfriendlyint():
    valid = False
    while valid == False:
        try:
            x = int(input('give me an int: '))
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

def antiblankyint():
    valid = False
    while valid == False:
        try:
            x = int(input('give me an int: '))
            valid = True
        except ValueError:
            print("Invalid Input!")
        except x == "":
            print("Invalid Input!")
    return x
    
def blankfriendlyfloat():
    valid = False
    while valid == False:
        try:
            x = float(input('give me a float: '))
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

def antiblankyfloat():
    valid = False
    while valid == False:
        try:
            x = float(input('give me a float: '))
            valid = True
        except ValueError:
            print("Invalid Input!")
        except x == "":
            print("Invalid Input!")
    return x

def blankfriendlystr():
    valid = False
    while valid == False:
        try:
            x = input('give me a string: ')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

def antiblankystr():
    valid = False
    while valid == False:
        try:
            x = input('give me a string: ')
#what??? i found this and it works, but how is 'empty string' even used???
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

def hello():
    print("hello")

def blanky_typeselect(type):
    if type == "string":
        x = blankfriendlystr()
        return x
    elif type == "float":
        x = blankfriendlyfloat()
        return x
    elif type == "int":
        x = blankfriendlyint()
        return x

def antiblanky_typeselect(type):
    if type == "string":
        x = antiblankystr()
        return x
    elif type == "float":
        x = antiblankyfloat()
        return x
    elif type == "int":
        x = antiblankyint()
        return x

def input_function(type, antiblanky):
    ret = ""
    if antiblanky == 1:
        ret = antiblanky_typeselect(type)
    else:
        ret = blanky_typeselect(type)
    return ret


    