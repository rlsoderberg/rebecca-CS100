"""
LOOK, THIS WHOLE THING ISN'T WORKING

#here, i'm putting all these searches in one program, right? today's weird thing?

#SEQUENTIAL SEARCH
#sequential search, you go through the whole haystack, one hay at a time

#here, i'm trying to do this without looking, let's see how it goes

def sequentialsearch(haystack, searchterm): #forgot arguments
    for i in range(0, len(haystack)): #still not sure why i have to do it this way
        if(haystack[i] == searchterm): #forgot parentheses OH, haystack[i] was key!!!!!!!!!!!!!!!!!!!!!
            return i

    return -1  

searchterm = input("enter a number between 1 and 10: ")
haystack = [3,5,6,7,2,4,9]

position = sequentialsearch(haystack, searchterm)


if position == -1:
    print(f"{searchterm} is not in the haystack")
else:
    print(f"i found {searchterm} at position {position}.")

"""

import random

def sequentialsearch(haystack, needle):
    for i in range(0, len(haystack)):
        if (haystack[i] == needle):
            return i

    return -1

def main():
    numbers = [3,5,6,7,2,4,9]

    target = int(input("enter a number between 1 and 10: "))
    location = sequentialsearch(numbers, target)
    if location == -1:
        print("couldn't find " + str(target))
    else:
        print("found " + str(target) + " at location " + str(location))


main()

#aha!!! i had to convert it to int!!! that is the key!!! bwahahahahaaaa