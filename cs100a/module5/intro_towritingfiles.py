#set a new variable equal to the filename, with 'w' for write, 'r' for read, or 'a' for append

#allow user to input filename
filename = input('please enter a filename to write to; ')
#request for user to input message to write to given filename
message = input(f'what message do you wish to write in {filename}? ')

#open a file, f
f = open(filename, 'w')
f.write(message)

#don't forget to close the file!
f.close()

