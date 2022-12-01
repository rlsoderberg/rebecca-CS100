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


#still does not allow going back and forth between range limitations
#wat is sandwich????

def sp(type):
    x = input()
    while x == "":
        print ("Out of range!")
        x = input(type)
    return x

def hello():
    print("hello")


def main(type, blankiness):
    if blankiness == True:
        if type == "str":
            x = sp(str())
        elif type == "float":
            x = sp(float())
        elif type == "int":
            x = sp(int())
    elif blankiness == False:
        if type == "str":
            x = str()
        elif type == "float":
            x = float()
        elif type == "int":
            x = int()
    return x

    