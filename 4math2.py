
#import python math module
import math

#welcome users to math.py
print("Welcome to math.py, version 2.")

#create array for list of int variables
int_array = []

#request user input of int variables
for s in range (0,3):
    valid = False
    while valid == False:
        try:
            int_array.append(int(input("Input an integer: ")))
            valid = True
        except ValueError:
            print("Invalid input.")

#perform arithmetic operations on int variables
if int_array[1] != 0:
    remainder = int_array[0] % int_array[1]
elif int_array[1] == 0:
    remainder = "undefined"
if int_array[0] != 0:
    quotient = int_array[2] / int_array[0]
elif int_array[0] == 0:
    quotient = "undefined"
difference = int_array[1] - int_array[2]

#create array for list of float variables
float_array = []

#request user input of float variables
for s in range (0,3):
    valid = False
    while valid == False:
        try:
            float_array.append(float(input("Input a float: ")))
            valid = True
        except ValueError:
            print("Invalid input.")

#perform arithmetic operations on float variables
product = float_array[0] * float_array[1]
if (float_array[1] + float_array[2]) != 0:
    diffmod = (float_array[2] + float_array[0]) % (float_array[1] + float_array[2])
elif (float_array[1] + float_array[2]) == 0:
    diffmod = "undefined"
powersum = float_array[0]**float_array[2] + float_array[1]**float_array[2]

#display arithmetic operations for int variables
print(type(int_array[0]))
print(int_array[0], " % ",int_array[1], " = ", remainder)
print(int_array[2]," / ", int_array[0], " = ", quotient)
print(int_array[1]," - ",int_array[2]," = ", difference)

#display arithmetic operations for float variables
print(type(float_array[0]))
print(float_array[0]," * ",float_array[1]," = ", product)
print("(",float_array[2]," - ",float_array[0],") % (",float_array[1]," - ",float_array[2],") = ", diffmod)
print(float_array[0],"**",float_array[2]," + ",float_array[1],"**",float_array[2]," = ", powersum)
