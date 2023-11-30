import os
import pathlib

#function to read madlib files
def madread(filename):
    f = open(filename, 'r')
    #empty string for story
    story = ''
    #for loop to print line by line
    for line in f:
        if line.startswith('*'):
            #text is where we store either the prompted user input, or the line
            text = input(f'give me a(n) {line.strip()}: ')
        else:
            text = line

        #add text to story
        story = story + ' ' + text.strip()

    print("here's your story:")
    #well, why is it giving me a one-word story? it ASKED me for all the lines... 
    #oh, i forgot to indent the storybuilding line...
    print(story)

    #don't forget to close your file!
    f.close()

#print introduction
print('which madlib file do you want to read as a madlib?')
#well, now i'm going to do my madlib selection 
#i had to duplicate the backslashes
for txt_file in pathlib.Path('C:\\Users\\rlsod\\rebeccaCS100\\cs100a\\module5').glob('*.txt'):
    print(txt_file)
    #what i also want to do, is check if the filename contains 'lib'
filename = input()
print(f'now reading {filename}')
madread(filename)


