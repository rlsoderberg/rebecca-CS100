import random

def sequentialsearch(haystack, needle):
    for i in range(0, len(haystack)):
        if(haystack[i] == needle):
            return i
    return -1

def main():
    numbers = []
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))

    target = random.randrange(0,2000)
    location = sequentialsearch(numbers, target)
    if location == -1:
        print("couldn't find ",str(target))
    else:
        print("found ",str(target)," at location ",str(location))

main()

