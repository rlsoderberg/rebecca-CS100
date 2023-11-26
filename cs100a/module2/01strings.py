#1.

#request for user to input a string
userstring = input('please input a string and press enter: ')

#request user choice of case conversion
valid = False
while valid == False:
    try:
        num = int(input('would you like to convert your string to 1) upper case, 2) lower case, or 3) title case? '))
        if num == "":
            raise ValueError('empty input')
        if num !=1 and num!=2 and num!=3:
            raise ValueError('input out of range')
        valid = True
    except ValueError:
        print('invalid input!')

#convert string to chosen case
if num == 1:
    print(userstring.upper())
elif num == 2:
    print(userstring.lower())
elif num == 3:
    print(userstring.title())

#remember to use the parentheses for the methods!

#2.

#request user to input link
weblink = input('please enter a web link: ')

#check if valid web link
if weblink.startswith('http'):
    print('you have entered a valid web link.')
else:
    print('you have entered an invalid web link.')

#3.

#request user to input name
name = input('please enter your name: ')

#print welcome text, using stripped name 
print(f'welcome, {(name.strip())}, to the program.')





