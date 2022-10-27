#factorial function
def factorialize(x):
    facto = 1
    for s in range (1, x+1):
        facto = facto * s
    return facto

#request user input
n = int(input("Enter a number: "))

#run function and print results
facto = factorialize(n)
print("Facto = ",facto)


