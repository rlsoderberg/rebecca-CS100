#1.

#request for user to input a string
userstring = input('please input a string and press enter: ')

#request user choice of case conversion
#i just stole this from an earlier answer, and this is legitimately a better way to do it, in this case
while case != '1' and case != '2' and case != '3':
    case = input('would you like to see the string in 1. upper case, 2. lower case, or 3. title case?')

#convert string to chosen case
if case == 1:
    print(userstring.upper())
elif case == 2:
    print(userstring.lower())
elif case == 3:
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

#reminder that you can strip specific things. how cool is that??
if name[-1] in ('a', 'e', 'i', 'o', 'u'):
    namestrip = name.strip('aeiou')
else:
    namestrip = name.strip('bcdfghjklmnpqrstvwxyz')
#welcome message, using stripped name
print(f'hello, {namestrip}, and welcome to the strip club')





