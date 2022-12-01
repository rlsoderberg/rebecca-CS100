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

def typeselector(type):
    if type == "str":
        x = input(str)
    elif type == "float":
        x = input(float)
    elif type == "int":
        x = input(int)

def blankiness(x, type):
    while x == "":
        print ("Out of range!")
        x = typeselector(type)
    return x

def main(type):
    x = typeselector(type)
    blankiness(x, type)
    return x


    