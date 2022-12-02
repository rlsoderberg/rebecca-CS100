#input functions
import sys
sys.path.append("C:..\..")
from i import hello
hello()
"""
def textselect(type):
    x = main(type)
    legit = False
    while legit == False:
        if x == "a" or x == "A":
            filename = "madlibtest.txt"
            return filename
            legit = True
        elif x == "b" or x == "B":
            filename = "koshism.txt"
            return filename
            legit = True
        elif x == "c" or x == "C":
            filename = "rockyhorror.txt"
            return filename
            legit = True
        else:
            print("Invalid Input!") 
            print("A, B, or C?")
            x = main(type)
"""
print('Welcome to CHOOSE YOUR MADLIB\nwill it be:')

#getting madlib selection
#REMINDER handle ranges externally
print('A)classic mad lib B)koshism C)rocky horror')
"""
type = "str"
filename = textselect(type)



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
"""