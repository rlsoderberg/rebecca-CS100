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

##input functions
def inputio():
    valid = False
    while valid == False:
        try:
            x =  input()
            while x == "":
                print("Out of range!")
                x = input()
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

#replacement section
for s in range (0,3):
    print("Pronoun: ")
    x = inputio()
    names.append(x)
    rand = random.choice(string.hexdigits)
    new = names[s].replace("e",rand)
    rand2 = random.choice(string.ascii_lowercase) + random.choice(string.digits) 
    new2 = new.strip(" htym")+rand2
    print("New pronoun: ",new2)
