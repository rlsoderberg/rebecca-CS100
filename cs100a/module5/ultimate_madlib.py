#right, so let me see if i can think, how to open the madlibtest
#first we need to open the file
f = open('themadlibtest.txt', 'r')

#introduce program
print('welcome to ULTIMATE MADLIB!')

print('\n\nplease enter: ')

#initialize word STRING
word_string = ''

#for loop, requesting word input for lines beginning with *
for line in f:
    if line.startswith('*'):
        user_word = input(line)
        word_string = word_string + ' ' + user_word
    elif line.startswith('/'):
        #look, i'm just trying to make it do nothing, how do i do that
        #does this work?
        continue
    else:
        word_string = word_string + ' ' + line

#close file
f.close()

#introduce madlib printing
print('\nnow we are ready to print your ULTIMATE MADLIB')

#for loop printing word array...
#oh wait!!! we want to store the words in a STRING, not a LIST
print(word_string)

#it's newlining strange!!!

"""

i just realized that all this stuff is uneccessary!!! we can just print word_array!!!

#initialize print word array
print_word_array = []

#for loop, printing all lines (except those beginning with /, which we will have to ignore)
for line in f:
    if line.startswith('/') or line.startswith(''):
        #look, i'm just trying to make it do nothing, how do i do that???
        print('')
    else:
        print_word_array.append(line)

print(print_word_array)"""






