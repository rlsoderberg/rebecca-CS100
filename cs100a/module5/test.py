f = open('madlibtest.txt', 'r')
#start with an empty string to store the story
story = ''
for line in f:
    if line.startswith('*'):
        #prompt the user for this thing.
        # Remove the *, and strip the whitespace
        text = input('Give me a(n) ' + line[1:].strip() + ': ')
    else:
        #just store the item
        text = line

    #whatever we have in text, add it to story
    story = story + ' ' + text.strip()

#now that we've built the story, let's read it
print("here's your story\n")
print(story)

f.close()



f = open('madlibstory.txt', 'w')
f.write(story)
f.close()