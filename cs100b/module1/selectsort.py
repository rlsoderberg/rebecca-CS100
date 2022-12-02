import random

def selectsort(list):
    for i in range(0, len(list)):
        min = i
        #look for an item smaller than list[min]
        for j in range(i, len(list)):
            if list[j] < list[min]:
                min = j     #just remember where this was
        #we've found it. Swap it into this location
        tmp = list[i]
        list[i]=list[min]
        list[min] = tmp

def main():
    numbers = []
    # let's make a list of random numbers
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))

    print(numbers[0:10])
    selectsort(numbers)
    print(numbers[0:10])
    print(__name__)

if __name__ == '__main__':
    main()
else:
    print("too far outside")