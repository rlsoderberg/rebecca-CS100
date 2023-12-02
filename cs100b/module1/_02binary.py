#binary search - sorted, using midpoint

import random

#we get start & end from haystack (assuming that 0 is the beginning)
def binarysearch(haystack, needle):
    start = 0
    end = len(haystack)

    #we want to go until start = end
    while start <= end:
        #i is midpoint
        i = start + (end - start)//2
        if haystack[i] < needle:
            start = i + 1
        elif haystack[i] > needle:
            end = i - 1
        else: 
            return i
        
    #return -1 if i not found
    return -1

def main():
    numbers = []
    #let's make a list of random numbers
    for f in range(0, 1000):
        numbers.append(random.randrange(0, 2000))

    #sort numbers so we can use binary search
    numbers.sort()
    #set target
    target = random.randrange(0, 2000)

    location = binarysearch(numbers, target)
    if location == -1:
        print(f"couldn't find {str(target)}")
    else:
        print(f'found {target} at {location}')

main()






