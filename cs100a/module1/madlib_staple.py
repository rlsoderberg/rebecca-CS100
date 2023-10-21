#ask user for name, welcome to staple removal program

name = input('what is your name? ')
print(f'hello, {name}. welcome to the staple_removal program.')

print("\nthe staple_removal program does not remove staples, but it's the thought that counts.")

#for some reason, there is a variable for staple removal
staple_removal = 0

#introduce the program, which tells you what to do with your files, depending on the years of the cases within
print('please input the earliest and latest year of the cases in your file')

#request input of file years
earliest = input("earliest year (don't try any funny business) ")
latest = input("latest year ")

#calculate how to react to various year ranges; print corresponding statements
if int(earliest) <= 2014 and int(latest) <= 2014:
    print('remove all files, and unstaple the header file')

elif int(earliest) <= 2014:
    print('remove all cases from 2014 and earlier')

#leave a statement for when nothing interesting happens
else:
    print('\nleave all files')

#we are also doing our madlib file
input("\nbut we're not stopping there. please get ready for a standard madlib. press any key to continue")

#print word requests
adjective = input("enter an adjective: ")
noun = input("enter a noun: ")
past_tense_verb = input("enter a past-tense verb: ")
noun2 = input("enter another noun: ")

#print full madlib sentence, including new words
print(f"\nthe quick, {adjective} {noun} {past_tense_verb} over the lazy {noun2}.\n")

#another madlib
print("please get ready for a galaxy-quest-themed madlib. press any key to continue")
input()

preposition = input("enter a preposition: ")
possessive_proper_noun = input('enter a possessive proper noun: ')
past_tense_transitive_verb = input('enter a past-tense transitive verb: ')

print(f'{preposition} {possessive_proper_noun} hammer, you shall be {past_tense_transitive_verb}.')






