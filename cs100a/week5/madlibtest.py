#input functions
import sys
sys.path.append("C:..\..")
from i import *
hello()

print('Welcome to CHOOSE YOUR MADLIB\nwill it be:')

#getting madlib selection
#REMINDER handle ranges externally
print('A)classic mad lib B)koshism C)rocky horror')

type = "str"
blanky = 1
x = main(type, blanky)
legit = False
while legit == False:
    if x == "a" or x == "A":
        filename = "madlibtest.txt"
        legit = True
    elif x == "b" or x == "B":
        filename = "koshism.txt"
        legit = True
    elif x == "c" or x == "C":
        filename = "rockyhorror.txt"
        legit = True
    else:
        print("Invalid Input!") 
        print("A, B, or C?")
        x = main(type, blanky)

#input / line transfer
f = open(filename, 'r')
story = ''
for line in f:

    if line.startswith('*'):
        text = input('Give me a(n) ' + line[1:].strip() + ': ')
    else:
        text = line
    story = story + ' ' + text.strip()

print("here's your story\n")
print(story)

f.close()

#store in madlibstory
f = open('madlibstory.txt', 'w')
f.write(story)
f.close()
