import string
import random

print("Gendered pronouns are so passe!")
print("Digitalize your pronouns with")
print("THE PRONOUN CONSTRUCTOR\n")
print("Please enter your current pronouns. ")
#tried to do for loop with empty array
s = 0
names = []
#multiple replace???
while (s < 3):
    x = input("Pronoun: ")
    names.append(x)
    if "e" in names[s]:
        new = names[s].replace("e","hg")
    rand = random.choice(string.ascii_lowercase + string.digits) 
    new = names[s].strip(" htsyr")+rand
    print(new)
    s+=1
