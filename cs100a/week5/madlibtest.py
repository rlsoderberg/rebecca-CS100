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
    while legit == False:
        if x == "a" or x == "A":
            legit = True
            filename = "madlibtest.txt"
        elif x == "b" or x == "B":
            legit = True
            filename = "koshism.txt"
        elif x == "c" or x == "C":
            legit = True
            filename = "rockyhorror.txt"
        else:
            print("Invalid Input!") 
            print("A, B, or C?")
            x = main(type)


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