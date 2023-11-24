#1. 

#create int and float variables; perform arithemtic operations
int1 = int(2)
int2 = int(3.5)
int3 = int(7.6)

float1 = float(6)
float2 = float(3.7)
float3 = float(0.5)

ans1 = int1+int2
print(f'int1 + int2 = {(int1 + int2)}')
ans2 = float2-int3
print(f'float2 - int3 = {ans2}')
#you need to put parentheses around calculations in an f string
print(f'float1*float3={(float1*float3)}')
print(f'float1/int1={(float1/int1)}')
print(f'int2%int3={(int2%int3)}')

#uh, the first time i tried performing calculations inside an f string, it didn't work

#you know, this 'many problems all in one file' thing was really only practical for the sql
#i'm just going to make a test file

#right!! you have to put the quotation marks OUTSIDE your, uh, interpolated value

#2. 

#set variable for bill
bill = 47.56
#display bill to user
print(f'your bill is ${bill}.')

#request for user to choose a tip amount
print("Please select a tip amount:")

#initialize tiplist and input variable
tiplist = [0, 10, 15, 20, 25]
i = 0

#limit input to given options
while i != '1' and i != '2' and i != '3' and i != '4':
    i = input(f'1. {tiplist[1]}% 2. {tiplist[2]}% 3. {tiplist[3]}% 4. {tiplist[4]}%  ')

#select tiplevel corresponding to input
tiplevel = tiplist[int(i)]

#calculate tip and total bill, based on tiplevel
tip = 0.01 * tiplevel * bill
total = bill + tip
print(f'your tip is ${tip}')
print(f'your total is ${total}')


#3.

#createe list of int games
gamelist = [45, 62, 35, 42, 31, 44]

#calculate & display point average
gametotal = 0
for x in range (0, 5):
    print(f'gamelist[{x}]={gamelist[x]}')
    gametotal += gamelist[x]
avg = gametotal / 5

print(f"diana's average point total in the last 5 games(rounded to the nearest whole number): {int(avg)}") 