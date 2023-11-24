import random

#11. 

ints = []

for x in range(0, 2):
    valid = False
    while valid == False:
        try:
            inp = int(input(f'please input integer #{(x + 1)}: '))
            ints.append(inp)
            if inp == "":
                raise ValueError ('empty input')
            valid = True
        except ValueError:
            print('invalid input')

#things i forgot
#put parentheses around expression in f string
#valid = True
#key thing: for the range of the for loop, create a range instead of going through empty list

print(f'int(#1) + int(#1) = {(ints[0] + ints[0])}')
print(f'int(#1) - int(#2) = {(ints[0]-ints[1])}')
print(f'int(#2) * int(#2) = {(ints[1]*ints[1])}')
if ints[1] != 0:
    print(f'int(#2) / int(#1) = {(ints[1]/ints[0])}')
    print(f'int(#1) % int(#2) = {(ints[0]%ints[1])}')
else:
    print("can't divide/mod by 0")

#12.

age = int(input('how old are you? '))

if age < 0:
    print('invalid age')
elif age >= 16:
    print('you can drive')
elif age >= 18:
    print('you can vote')
elif age >= 21:
    print('you can enjoy a beer')
elif age >= 55:
    print('you can get the senior discount')

#13.

stop = 0
while stop == 0:
    usermove = int(input('rock (1), paper(2), or scissors(3)? '))
    compmove = random.randrange(1, 4)
    moves = [0, 'rock', 'paper', 'scissors']

#i'm rewriting this, and it's really long again!!! my cool algorithm depended on modifying rps order, right?
    win = ''
    if usermove == 1:
        if compmove == 3:
            win = 'u'
        elif compmove == 2:
            win = 'c'
        elif compmove == 1:
            win = 't'
    elif usermove == 2:
        if compmove == 3:
            win = 'c'
        elif compmove == 2:
            win = 't'
        elif compmove == 1:
            win = 'u'
    elif usermove == 3:
        if compmove == 3:
            win = 't'
        elif compmove == 2:
            win = 'u'
        elif compmove == 1:
            win = 'c'

    if win == 'u': 
        print(f'user({moves[usermove]}) defeats computer({moves[compmove]})')
    elif win == 'c':
        print(f'user({moves[usermove]}) is defeated by computer({moves[compmove]})')
    elif win == 't':
        print(f'user({moves[usermove]}) ties with computer({moves[compmove]})')

    valid = False
    while valid == False:
        try:
            stop = int(input('press 1 to stop, or 0 to continue: '))
            if stop == "":
                raise ValueError('empty input')
            if stop > 1: 
                raise ValueError('input out of range')
            valid=True
        except ValueError:
            print('invalid input! ')

#and remember to get the range right!



    


        
        
    

