def int():
    valid = False
    while valid == False:
        try:
            x = int(input('give me an int: '))
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x


def float():
    valid = False
    while valid == False:
        try:
            x = float(input('give me a float: '))
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

def str():
    valid = False
    while valid == False:
        try:
            x = input('give me a string: ')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

def hello():
    print("hello")

def typeselect(type):
    if type == "str":
        x = str()
        return x
    elif type == "float":
        x = float()
        return x
    elif type == "int":
        x = int()
        return x

def blankiness(x, type):
    while x == "":
        print ("Out of range!")
        x = typeselect(type)
    return x

def maine(type, blanky):
    x = typeselect(type)
    ret = ''
    if blanky == 1:
        ret = blankiness(x, type)
    return ret


    