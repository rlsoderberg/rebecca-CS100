import random

#what do you mean 'try it with letters', when there are 26 letters, but 2000 numbers?
#i think last time i used words, and i was tempted to do that again
#idk, im not getting much done today, i will come back tomorrow

def randomstrings():
    letters = "abcdefghijklmnopqrstuvwxyz"
    #list of randomstrings
    strings = []

    for i in range(1,1000):
        #length of randomstring
        length = random.randrange(5, 15)
        randomstring = ""
        for c in range (0, length):
            #pick random letters from letters
            i = random.randrange(0, len(letters))
            randomstring = randomstring + letters[i]
        #add randomstrings to strings list
        strings.append(randomstring)
    return strings


#sequential search is just a normal search that goes sequentially in a for loop or something
def sequentialsearch(haystack, needle):
    for i in range(0, len(haystack)):
        if haystack[i] == needle:
            return i
    return -1

#look for location of random number which has a like 50% chance of being in the random range
def main():
    strings = randomstrings()
    
    target = random.randrange(0, 2000)
    location = sequentialsearch(strings, target)
    if location == -1:
        print("couldn't find " + str(target))
    else:
        print("found " + str(target) + " at location " + str(location))

main()
