import sys
sys.path.append('../..')

from i import maine

type = "int"
antiblanky = 1

def check(s):
    #how do i pick which variable i am checking????
    print("press 1 to guess a variable, and press 2 to continue to the next operation")
    action = maine(type, antiblanky)
    while action == 1: #is this even the right way to do it???
        guess = maine(type, antiblanky)
        if guess == #the right answer?????:
            print("Correct!")
        elif guess != #the right answer?????:
            print("Incorrect!")
        print("press 1 to guess a variable, and press 2 to continue to the next operation")
        action = maine(type, antiblanky)




def label(count):
    count += 1
    print("Operation "+count+": ")




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
sum = x + y + z
difference = z - y - x
product = x * y * z
quotient = (x + y) / z
mod = (y-z)%x
power = x**z + y**z

count = 0

#display arithmetic operations for int variables
print("1. Arithmetic operations performed on "+ type(x)+ "variable")
label(count)
print("x + y + z = ", sum)
check(s) #see, what i need to do, is put the variables in, like, a set or something? maybe also make them so i can referece them? idk!!!
#and also, i need to be looping through the problems!!!
# AND i need to tidy up my input function!!!
print("x - y - z = ", difference)
print("x * y * z = ", product)
print("(x + y)/z = ", quotient)
print("(y - z) % x = ", mod)
print("x**z + y**z = ", power)

#perform arithmetic operations on float variables
sum = x + y + z
difference = x - y - z
product = x * y * z
quotient = (x + y)/z
mod = (y - z) % x
power = x**z + y**z

count = 0



#display arithmetic operations for float variables
print("1. Arithmetic operations performed with "+ type(a))+ "variable")
print("x - y - z = ", difference)
print("x * y * z = ", product)
print("(x + y)/z = ", quotient)
print("(y - z) % x = ", mod)
print("x**z + y**z = ", power)


