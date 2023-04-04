import random

def randomstrings(letters):
    #list of randomstrings
    strings = []

    for i in range(0,10000):
        #length of randomstring
        length = random.randint(1,4)
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
    bigwordcount = 0
    bigwords = []
    for x in range (0, 50):
        letters = "abcdefghijklmnopqrstuvwxyz"
        strings = randomstrings(letters)
        target = ""
        length = random.randint(1,4)
        for a in range (0, length):
            rand = random.randrange(0, len(letters))
            target = target + letters[rand]
        print("looking for "+str(target))
        for i in range (0, 10000):
            location = sequentialsearch(strings, target)
        if location == -1:
            print("couldn't find " + str(target))
        else:
            print("found " + str(target) + " at location " + str(location))
            if len(target) >= 3:
                print("congratulations! you found a big word!")
                bigwordcount += 1
                bigwords.append(target)
    print("i searched 50 times and i found "+str(bigwordcount)+" big words: "+str(bigwords))

    

main()
