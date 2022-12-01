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
#still not sure what to do with these!!!!
def rng(x):
    while x < 0:
        print ("Out of range!")
        #????
    return x

def sp(x):
    while x == "":
        print ("Out of range!")
        #????
    return x

def hello():
    print("hello")


