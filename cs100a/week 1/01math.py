#welcome users to math.py
print("Welcome to math.py. \n Can you guess the variables?")

#create int variables
x = 7
y = 4
z = 26

#create float variables
a = 9.3
b = 2.6
c = 15.7

#perform arithmetic operations on int variables
remainder = x % y
quotient = z / x
difference = y - z

#perform arithmetic operations on float variables
product = a * b
diffmod = (c - a) % (b - c)
powersum = a**c + b**c

#display arithmetic operations for int variables
print(type(x))
print("x % y = ", remainder)
print("z / x = ", quotient)
print("y - z = ", difference)

#display arithmetic operations for float variables
print(type(a))
print("a * b = ", product)
print("(c - a) % (b - c) = ", diffmod)
print("a**c + b**c = ", powersum)

