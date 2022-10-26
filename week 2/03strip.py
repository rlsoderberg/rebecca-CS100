import string
import random
#introduce program, request user input
print("Gendered pronouns are so passe!")
print("Digitalize your pronouns with")
print("THE PRONOUN CONSTRUCTOR\n")
print("Please enter your current pronouns. ")
#initialize pronoun counter, pronoun array
s = 0
names = []
#i'm not exactly sure where i needed to use x, vs. names[s]???
#construct new pronoun for each of the user's pronouns, using replace and random characters
for s in range (0,3):
    x = input("Pronoun: ")
    names.append(x)
    rand = random.choice(string.hexdigits)
    new = names[s].replace("e",rand)
    rand2 = random.choice(string.ascii_lowercase) + random.choice(string.digits) 
    new2 = new.strip(" htym")+rand2
    print("New pronoun: ",new2)
