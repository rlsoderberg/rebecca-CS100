#right, so let me see if i can think, how to open the madlibtest
#first we need to open the file
f = open('themadlibtest.txt', 'r')

#introduce program
print('welcome to ULTIMATE MADLIB!')

print('\n\nplease enter: ')

#initialize word string
word_string = ''

#for loop, requesting word input for lines beginning with *
for line in f:
    if line.startswith('*'):
        user_word = input(line)
        word_string = word_string + ' ' + user_word
    else:
        word_string = word_string + ' ' + line

#close file
f.close()

#introduce madlib printing
print('\nnow we are ready to print your ULTIMATE MADLIB')

#print the madlib string
print(word_string)

#it's newlining strange!!!






