#import random to generate randomized list
import random

def insertion_sort(list):
    #i is unchanging position marker
    for i in range(1, len(list)):
        #pos is changing position marker
        pos = i
        #number is unchanging list value corresponding to i
        number = list[i]
        #slide numbers to right if number is lower
        while pos > 0 and list[pos - 1] > number:
            list[pos] = list[pos - 1]
            pos = pos - 1
        #this line just takes care of end
        list[pos] = number

#define function to generate random number string
def number_list():
    list = []
    for x in range (0, 50):
        r = random.randrange(100)
        list.append(r)
    return list

#generate random number list
list = number_list()
#sort list with insertion sort function
insertion_sort(list)
#display results
print(f'sorted list: {list}')