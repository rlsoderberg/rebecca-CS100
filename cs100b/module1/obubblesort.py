import random

def bubblesort(list):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(list)-1):
            if list[i] > list[i+1]:
                swap = True
                tmp = list[i]
                list[i] = list[i+1]
                list[i+1]=tmp

numbers = []
for i in range(0, 1000):
    numbers.append(random.randrange(0,2000))

print(numbers[0:10])
bubblesort(numbers)
print(numbers[0:10])

x = open('words.txt','r')
words = (x.read())
array = words.split()

print(array[0:10])
bubblesort(array)
print(array[0:10])
