import random

def binarysearch(needle, haystack):
    start = 0
    end = len(haystack)

    while start <= end:
        #here is the binary part!! gleaming with the sheen of FLOOR DIVISION
        i = start + (end-start)//2
        #my search was acting so weird, and you know what i did? i wrote <=!!! bad!!!
        if haystack[i] < needle:
            start = i+1
        elif haystack[i] > needle:
            end = i-1
        else:
            return i

    #if we're out of the loop, we didn't find it
    return -1

def main():
    numbers = []
    # let's make a list of random numbers
    haystack = []
    for i in range(0,100):
        rand = random.randrange(0,200)
        haystack.append(rand)
    #remember to sort your haystack!!!!!!!!!!!!!!!!!!
    haystack.sort()
    needle = random.randrange(0,200)
    #is it good form to use the same exact variables when i call a function and when i define it?
    #i do that a lot and i am not sure whether it is a good idea
    location = binarysearch(needle, haystack)
    if location == -1:
        print("couldn't find " + str(needle))
    else:
        print("found " + str(needle) + " at location " + str(location))

main()




