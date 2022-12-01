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

def blankiness():
    x = input()
    while x == "":
        print ("Out of range!")
        x = input(type)
    return x

def hello():
    print("hello")


def main(type, blankiness):
    #I WANT TO DO SOMETHING WITH BLANKINESS BUT I'M NOT SURE HOW WITHOUT A BUNCH OF COPY PASTING OR SOMETHING
    #wondering, is blankiness something I should put on the outside?
    if type == "str":
        x = input(str())
    elif type == "float":
        x = input(float())
    elif type == "int":
        x = input(int())
    return x

    