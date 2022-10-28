#input functions
def inputio():
    valid = False
    while valid == False:
        try:
            n = int(input("Enter a number: "))
            valid = True
        except ValueError:
            print("Invalid Input!")
    return n

def input2():
    x = inputio()
    while x == "":
        print("I didn't hear you!")
        x = inputio()
    return x

#factorial function
def factorialize(x):
    facto = 1
    for s in range (1, x+1):
        facto = facto * s
    return facto

#request user input
n = input2()


#run function and print results
facto = factorialize(n)
print("Facto = ",facto)


