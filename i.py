def input(type):
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

#is this even the right way to reference an argument???
    if type == "str":
        x = str()
        return x
    elif type == "float":
        x = float()
        return x
    elif type == "int":
        x = int()
        return x

#still does not allow going back and forth between range limitations
#wat is sandwich????

def rng(type):
    #what about custom ranges
    while x < 0:
        print ("Out of range!")
        x = input(type)
    return x

def sp(type):
    while x == "":
        print ("Out of range!")
        x = input(type)
    return x

def hello():
    print("hello")


