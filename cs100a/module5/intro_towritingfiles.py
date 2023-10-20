#ok, i kind of remembered this, half glancing at the examples
#what i forgot was 1) you need to equal the open to something
#and 2) you need to put 'w' or 'r' in quotes
#apparently the otehr one is 'a', which appends to a file

#allow user to input filename
filename = input('please enter a filename to write to; ')
#so what do you mean exactly, 'it could be a literal value or a string variable'?
message = input(f'what message do you wish to write in {filename}? ')

#open a file, f
f = open(filename, 'w')
f.write(message)

#don't forget to close the file!
f.close()

