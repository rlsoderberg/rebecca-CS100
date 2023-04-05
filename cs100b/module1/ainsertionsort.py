#like bubble sort, compares adjacent values, but you also shift the rest of the values
def insertionsort(list):
    for i in range(1, len(list)):
        number = list[i]
        pos = i
        #look at this! built in tmp!
        while pos > 0 and list[pos-1] > number:
            list[pos] = list[pos - 1]
            pos = pos - 1
        list[pos] = number
