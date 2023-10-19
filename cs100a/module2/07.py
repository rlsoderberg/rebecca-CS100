#right, i guess it's pretty impractical to put multiple problems in the same program

#7

#let me see if i can remember, is this one getint()???

#request for user to input a string
string = input("please enter a string (it's more fun if it contains numbers): ")

#no, i don't think it's getint() at all
#oh,,, isdigit()
#getint() is a thing in java, apparently? 
#i should totally take java next, but omg can i pls just get a job already?

"""digits = string.isdigit()
print(digits)

well, i did this, and it returned false. ummm...

wait, isdigit isn't what i want!!!

oh i see, i'd better put it in a loop"""

#initialize digit total
total = 0

#do for loop of characters in string
#for x in range (0, len(string)): ah, little did i know, you can loop directly through a string
for char in string:
    if char.isdigit():
        #do not forget to make inty!!!
        total += int(char)

#display total of digits in string
print(f"total of digits in string '{string}' is {total}.")