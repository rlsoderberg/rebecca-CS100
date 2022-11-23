import random
import urllib.request

x = urllib.request.urlopen("https://www.mit.edu/~ecprice/wordlist.10000")
words = (x.read())
array = words.split()

def sequentialsearch(haystack, needle):
    for i in range(0, len(haystack)):
        if(haystack[i] == needle):
            return i
    return -1

def main():
    words5000 = []
    for i in range(0, 5000):
        rand10 = random.randrange(0,10000)
        words5000.append(array[rand10])

    target = random.randrange(0,10000)
    targetword = array[target]
    location = sequentialsearch(words5000, targetword)
    if location == -1:
        print("couldn't find ",str(targetword))
    else:
        print("found ",str(targetword)," at location ",str(location))

main()

