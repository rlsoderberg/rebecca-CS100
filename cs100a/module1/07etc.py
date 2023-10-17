#we are also asking for name down here because it should be pretty short
#we are actually putting this at the top so that it is not entirely disappointing

name = input('what is your name? ')
print(f'hello, {name}. welcome to the staple_removal program.')

print("\nthe staple_removal program does not remove staples, but it's the thought that counts.")

#here's the one where i have to think of a situation!!!
#lately i've taken to sorting files a couple hours a week
#if only i could apply that level of diligence to the management of my schedule
#so we're going to make a file sorting timer, right?

staple_removal = 0

print('please input the earliest and latest year of the cases in your file')
#list appends to the right. but we don't care because we only need 2 values!!! we don't even need a list!!!
#well, i took out the list because it was being funny. maybe it was type alignment, idk
earliest = input("earliest year (don't try any funny business) ")
latest = input("latest year ")

if int(earliest) <= 2014 and int(latest) <= 2014:
    print('remove all files, and unstaple the header file')

elif int(earliest) <= 2014:
    print('remove all cases from 2014 and earlier')

#don't forget to leave a case for when nothing interesting happens!!!
else:
    print('\nleave all files')



#i don't know how to complete this program, but i do now realize i need a staple remover
#the benefits of writing programs about real life!!!

print("\nbut we're not stopping there. please get ready for a standard madlib. press any key to continue")
#x = () this was how i had press any key to continue before
#i had to go look at risk
#oh!!! of course that wasn't working!!!
input()

adjective = input("enter an adjective: ")
noun = input("enter a noun: ")
past_tense_verb = input("enter a past-tense verb: ")
noun2 = input("enter another noun: ")

print(f"\nthe quick, {adjective} {noun} {past_tense_verb} over the lazy {noun2}.\n")

print("please get ready for a galaxy-quest-themed madlib. press any key to continue")
input()

preposition = input("enter a preposition: ")
possessive_proper_noun = input('enter a possessive proper noun: ')
past_tense_transitive_verb = input('enter a past-tense transitive verb: ')

print(f'{preposition} {possessive_proper_noun} hammer, you shall be {past_tense_transitive_verb}.')






