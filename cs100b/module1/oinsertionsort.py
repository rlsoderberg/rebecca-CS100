def insertionsort(list):
    for i in range(1, len(list)):
        number = list[i]
        pos = i
        while pos > 0 and list[pos-1] > number:
            list[pos] = list[pos - 1]
            pos = pos - 1
        list[pos]=number

x = open("words.txt", "r")
words = (x.read())
array = words.split()

print(array[0:10])
insertionsort(array)
print(array[0:10])
