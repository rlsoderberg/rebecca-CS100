f = open("madlibtest.txt", "r")
#empty string to store story
story = ''

lineno = 1
madlib = ""
for line in f:
    if line.startswith("*"):
        #output as command, strip
        newline = text = input('Give me a(n) ' + line[1:].strip() + ': ')
        #put newline onto madlib
        madlib += (" " + newline)
    elif not line.startswith("*"):
        #put lint onto madlib
        madlib += (" " + line)
#why is my madlib so awkward looking?
print("here is your madlib: "+madlib)
f.close()

import os

#get path of this directory (because i sure don't know it)
dir_path = os.getcwd()
#put all filenames into dir_list
dir_list = os.listdir(dir_path)

#make list for text files
txt_files = []
for f in dir_list:
    #filter by those ending in .txt
    if f.endswith(".txt"):
        txt_files.append(f)

#print text files
print("text files in this directory:")
for t in txt_files:
    print(t)