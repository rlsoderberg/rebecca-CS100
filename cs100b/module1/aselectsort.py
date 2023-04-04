def selectionsort(list):
    for i in range(0, len(list)):
        min = i
        for j in range (i, len(list)):
            if list [j] < list[i]:
                min = j
        tmp = list[i]
        list[i]=list[min]
        list[min]=tmp

import random 

def main():
    numbers = []
    for i in range (0, 1000):
        numbers.append(random.randrange(0,2000))
    
    print(numbers[0:10])
    selectionsort(numbers)
    print(numbers[0:10])

    if __name__ == "__main__":
        main()

