import random

#bubble sort swaps adjacent values
def bubblesort(list):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(list) - 1):
            if list[i] > list[i + 1]:
                swap = True
                tmp = list[i]
                list[i] = list[i+1]
                list[i+1] = tmp

def main():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    strings = []
    print(letters)
    for i in range (0, 10):
        strings.append(letters[random.randrange(0,len(letters))])
    
    print(strings[0:10])
    bubblesort(strings)
    print(strings[0:10])

if __name__ == "__main__":
    main()

