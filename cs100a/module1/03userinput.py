#4.

print('please input 6 digits of any kind (int or float):')
inp = []

for x in range(0, 7):
    valid = False
    while valid == False:
        try:
            result = float(input(f'#{x}: '))
            if result == "":
                raise ValueError ('empty string')
            valid = True
        except ValueError:
            print('invalid input!')
    inp.append(result)
#here, i'm trying to forbid blank input & non-numerical input, but i still get errors from those things!!
#OH, i forgot valid = false AND i needed to put append result outside the try except
#or, well, i don't know if i NEED to put append result outside, but it seems more correct

#remember to append whenever you have an empty list
#also don't use input as a variable name...

print(f'int(#1) + int(#2) = {(int(inp[1]) + int(inp[2]))}')
#you need to put parentheses around calculations in an f string
print(f'float(#5) - int(#3) = {(float(inp[5])-int(inp[3]))}')
print(f'float(#2) * float(#6) = {(float(inp[2])*float(inp[6]))}')
print(f'float(#4) / int(#4) = {(float(inp[4])/int(inp[4]))}')
print(f'int(#5) % int(#6) = {(int(inp[5])%int(inp[6]))}')

#5.

#get user input for bill
valid = False
while valid == False:
    try:
        bill = float(input("please input bill: "))
        if bill == "":
            raise ValueError('empty input')
        valid = True
    except ValueError:
        print('invalid input!')

#display bill to user
print(f'your bill is ${(round(bill, 2))}.')
#remember to put it in parentheses, and make bill a float to begin with

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

#6.

#introduce score request loop
print(f"i will ask of you diana's score totals in the last 5 games.")

#initialize list of int games
gamelist = []

#int input function
for x in range (0, 5):
    valid = False
    while valid == False:
        try:
            newgame = int(input(f'score {x}: '))
            if newgame == "":
                raise ValueError('empty string')
            gamelist.append(int(newgame))
            print(f'gamelist[{x}] = {newgame}')
            w = True
        except ValueError:
            print("invalid Input")
    x+=1

#calculate & display point average
gametotal = 0
for x in range (0, 5):
    print(f'gamelist[{x}]={gamelist[x]}')
    gametotal += gamelist[x]
avg = gametotal / 5

print(f"diana's average point total in the last 5 games(rounded to the nearest whole number): {int(avg)}") 

#7.

#oh, i know, i need to write a mug cake program...

valid = False
while valid == False:
    try:
        mugnum = int(input('how many mugs? '))
        valid = True
    except ValueError:
        print('invalid input!')

recipe = [(1, 'tbsp', 'butter'),(2, 'tbsp', 'sugar'), 
          (3, 'tbsp', 'milk'), (2, 'tbsp', 'lemon juice'), 
          (4, 'tbsp', 'flour'), (0.5, 'tsp', 'baking soda'),
          (0.125, 'tsp', 'salt')]

for x in recipe:
    newnum = (mugnum * x[0])
    newmsr = x[1]
    if newmsr == 'tbsp':
        if newnum >= 16:
            newnum = (newnum/16)
            newmsr = 'cups'
    elif newmsr == 'tsp':
        if newnum >= 48:
            newnum = (newnum/48)
            newmsr = 'cups'
        elif newnum >= 3:
            newnum = (newnum/3)
            newmsr = 'tbsp'
    print(f'{newnum} {newmsr} {x[2]}')

#8.

name = input('what is your name? ')
print(f'{name}, welcome to the program.')

#9.

adjective = input('please input an adjective: ')
subject = input('please input a noun: ')
verb = input('please input a past-tense verb: ')
object = input('please input a noun: ')

print(f'the quick, {adjective} {subject} {verb} over the lazy {object}.')

#this is an og classic soderberg madlib!!!
print(f'{plant} {gerund} us on a scooter with {watercraft} {machine}')

#10.

plant = input('please input a flowering plant (singular): ')
gerund = input('please input a gerund: ')
watercraft = input('please input a personal watercraft: ')
machine = input('please input a simple machine (pural): ')

#this is an og classic soderberg madlib!!!
print(f'{plant} {gerund} us on a scooter with {watercraft} {machine}')