def int():
    valid = False
    while valid == False:
        try:
            x = int(input())
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x


def float():
    valid = False
    while valid == False:
        try:
            x = float(input())
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

def str():
    valid = False
    while valid == False:
        try:
            x = input()
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

def main(type, blanky):
    x = typeselect(type)
    if blanky == 1:
        blankiness(x, type)
    return x


    