import random

#binary search function. i tried to make it more binary but then it kept freezing! wat???
def binarysearch(haystack, needle):
    start = 0
    end = len(haystack)
    while start <= end:
        i = start + (end-start)//2
        if haystack[i] < needle:
            start = i + 1
        elif haystack[i] > needle:
            end = i - 1
        else:
            return i
"""
    while start <= end:
        i = start + (end-start)//2
        if haystack[i] < needle:
            start = i + (end - i)//2
        elif haystack[i] > needle:
            end = i - (i - start)//2
        else:
            return i
"""


def main():
    numbers = []
    # let's make a list of random numbers
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))

    # sort the numbers so we can use binary search
    numbers.sort()
    target = random.randrange(0,2000)
    #now it sometimes gives none as a location??? wat even is binary search
    location = binarysearch(numbers, target)
    if location == -1:
        print("couldn't find " + str(target))
    else:
        print("found " + str(target) + " at location " + str(location))

main()

