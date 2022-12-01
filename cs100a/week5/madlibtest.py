def textselect(x):
    if x == "a" or x == "A":
        x.filename = "madlibtest.txt"
        x.truth = True
    elif x == "b" or x == "B":
        x.filename = "koshism.txt"
        x.truth = True
    elif x == "c" or x == "C":
        x.filename = "rockyhorror.txt"
        x.truth = True
    else:
        return False
        print("Invalid Input!") 
        print("A, B, or C?")

#input functions
import sys
sys.path.append("C:..\..")
from i import *
hello()


print('Welcome to CHOOSE YOUR MADLIB\nwill it be:')

#getting madlib selection
legit = False
while legit == False:
    #REMINDER handle ranges externally
    print('A)classic mad lib B)koshism C)rocky horror')
    type = "str"
    x = main(type)
    textselect(x)
    while x.truth == False:
        x.truth = textselect(x)

#input / line transfer
f = open(x.filename, 'r')
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