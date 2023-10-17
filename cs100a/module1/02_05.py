#so this second set of problems add onto themselves, so i'll problem 2 for both variables & user input

bill = 47.56
print(f'your bill is ${bill}.')

#oh boy, if i'm doing this from memory, i have to write this input function over and over again
#that's one way to remember it

"""valid = False
while valid == False:
    try:
        #like, i'm using float i guess? since that takes both int and float, right?
        #tip 

        #oh wait oh wait, i don't have to do that whole thing, this could be a lot easier"""


print("Please select a tip amount:")

"""tip = 'x'
while tip != 'a' and tip != 'b' and tip != 'c' and tip != 'd':
    tip = input('a. 10% b. 15% c. 20% or d. 25%?')"""
#wait wait wait, i see, maybe there's a way i can hook up a list with this input thing

tiplist = [0, 10, 15, 20, 25]
i = 0
while i != '1' and i != '2' and i != '3' and i != '4':
    i = input(f'1. {tiplist[1]}% 2. {tiplist[2]}% 3. {tiplist[3]}% 4. {tiplist[4]}%  ')
#see, it's now i kind of wish i could convert letters into ints, like a=1, b=2...
#it seems like there's supposed to be a way to do that. how do i do that???

#oh, i kind of stepped around that problem by using numbers instead of letters. still curious about conversion
#although i really can't tell how relevant it is!!!

tiplevel = tiplist[int(i)]

#there are a lot of different variables starting with 'tip'... kind of confusing i guess!!!
#i'm replacing tipnum with input... input isn't one of those weird words in python, is it???

#i think it might have indeed been one of those weird words. oh dear, i'm saving that one for posterity
tip = 0.01 * tiplevel * bill
total = bill + tip
print(f'your tip is ${tip}')
print(f'your total is ${total}')

