#input functions
def inputio():
    valid = False
    while valid == False:
        try:
            x =  int(input())
            while x == "":
                print("Out of range!")
                x = int(input())
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

#factorial function
def factorialize(x):
    facto = 1
    for s in range (1, x+1):
        facto = facto * s
    return facto

#request user input
print("Enter a number: ")
n = inputio()


#run function and print results
facto = factorialize(n)
print("Facto = ",facto)


