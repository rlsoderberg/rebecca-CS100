import random

#binary search function. i got it to go a little faster i guess???
def binarysearch(haystack, needle):
    start = 0
    end = len(haystack)

    position = -1
    while position == -1:
    #still not working... need to, like, set up a good thing that points to return -1
        i = start + (end-start)//2
        print(abs(i-end))
        #although it keeps printing the same abs values!!! what is the deal with that???
        if(abs(i-end) > 1):
            if haystack[i] < needle:
                start = i+(end - i)//2
            elif haystack[i] > needle:
                end = i-(i - start)//2
        else:
            return i
            position = i
    return -1


def main():
    numbers = []
    # let's make a list of random numbers
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))

    # sort the numbers so we can use binary search
    numbers.sort()
    target = random.randrange(0,2000)
    #well, now it keeps always finding target!!! 
    location = binarysearch(numbers, target)
    if location == -1:
        print("couldn't find " + str(target))
    else:
        print("found " + str(target) + " at location " + str(location))

main()

