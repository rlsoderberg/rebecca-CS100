import random
import urllib.request



def selectionsort(list):
    for i in range(0, len(list)):
        min = i
        #look for a word shorter than list[min]
        for j in range(i, len(list)):
            if len(list[j]) < len(list[min]):
                min = j     #just remember where this was
        #we've found it. Swap it into this location
        tmp = list[i]
        list[i]=list[min]
        list[min] = tmp

def main():
    # let's make a list of random words
    x = urllib.request.urlopen("https://www.mit.edu/~ecprice/wordlist.10000")
    words = (x.read())
    array = words.split()

    print(array[0:10])
    selectionsort(array)
    print(array[0:10])

if __name__ == '__main__':
    main()
else:
    print("too far outside")