#picks first number and compares to all until finds new min/max, then second number, etc
def selectionsort(list):
    for i in range(0, len(list)):
        min = i
        for j in range (i, len(list)):
            #oooops, list[j] < list[min], i was using [i] instead of [min] and it kind of half worked
            if list [j] < list[min]:
                min = j
        tmp = list[i]
        list[i]=list[min]
        list[min]=tmp

import random 

def main():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    strings = []
    print(letters)
    for i in range (0, 10):
        strings.append(letters[random.randrange(0,len(letters))])
    
    print(strings[0:10])
    selectionsort(strings)
    print(strings[0:10])

if __name__ == "__main__":
    main()

