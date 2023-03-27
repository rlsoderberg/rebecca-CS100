#request user input of integers
int1 = int(input("Enter Integer 1: "))
int2 = int(input("Enter Integer 2: "))

#perform calculations
sum = int1 + int2
difference = int2 - int1
product = int1 * int2

#display results, as possible
if int2 != 0:
    quotient = int2 / int1
    remainder = int2 % int1
    print(int1," + ",int2," = ",sum,". ",int2," - ",int1," = ",difference,". ",int1," * ",int2," = ",product,". ",int2," / ",int1," = ",quotient,". ",int2," % ",int1," = ",remainder,". ")

else:
    print("Can't divide by 0! Here are the functions that don't divide by 0:")
    print(int1," + ",int2," = ",sum,". ",int2," - ",int1," = ",difference,". ",int1," * ",int2," = ",product,". ")