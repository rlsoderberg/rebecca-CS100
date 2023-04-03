f = open("madlibtest.txt", "r")
#empty string to store story
story = ''

lineno = 1
madlib = ""
for line in f:
    if line.startswith("*"):
        #output as command, strip
        text = input('Give me a(n) ' + line[1:].strip() + ': ')
    elif not line.startswith("*"):
        #put lint onto madlib
        text = (" " + line)

    #put newline onto madlib
    madlib += (" " + text.strip())
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