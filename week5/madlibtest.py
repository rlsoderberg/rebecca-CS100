print('Welcome to CHOOSE YOUR MADLIB\nwill it be:\nA)classic mad lib B)koshism C)rocky horror')

f = open('madlibtest.txt', 'r')
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

f = open('madlibstory.txt', 'w')
f.write(story)
f.close()