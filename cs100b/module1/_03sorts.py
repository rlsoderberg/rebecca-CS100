#selection sort - SELECT an item smaller than minimum, swap with minimum (far reaching hand)
#bubble sort - swap adjacent pairs, if they need to be swapped. the swapping goes around like a BUBBLE
#insertion sort - INSERT card, slide cards over, as long as they are smaller

import random 

def selectionsort(list):
    for i in range(0, len(list)):
        min = i
        #look for an item smaller than list[min]
        for j in range(i, len(list)):
            if list[j] < list[min]:
                #record the first instance of a number being smaller than list[min]
                min = j
        #hand reaches over and swaps list[i] with list[min](now list[j])
        tmp = list[i]
        list[i] = list[min]
        list[min] = tmp

def bubblesort(list):
    for i in range(0, len(list)):
        #this little True/False thing, this looks so weird
        #but since it's inside a for loop... all it's doing is...
        #it swaps until it stops.
        swap = True
        while swap:
            swap = False
            #every turn, we sort from the beginning
            for i in range(0, len(list)-1):
                #here we are doing potential bubbles
                if list[i] > list[i+1]:
                    swap = True
                    tmp = list[i]
                    list[i] = list[i+1]
                    list[i+1] = tmp

def insertionsort(list):
    #we start at 1 because we look backwards
    for i in range(1, len(list)):
        #we set number as the value of list[i]
        number = list[i]
        #we can shift our position, wherever the cards take us
        pos = i
        #we make sure that pos is greater than 0(even though it should be)
        while pos > 0 and list[pos - 1] > number:
            #if list[pos - 1] is greater, then we shift the value of list[pos] back
            list[pos] = list[pos - 1]
            pos = pos - 1
        #so whatever value we stopped at, we want to put that in the bottom because it didn't get swapped???
        #no, like, i've hand sorted this one enough, i think i get it, it's just kind of hard to explain
        #this one is the most fun to hand sort
        list[pos] = number


def main():
    numbers = []
    #let's make a list of random numbers
    for i in range(0, 1000):
        numbers.append(random.randrange(0, 1000))

    print(numbers[0:10])
    insertionsort(numbers)
    print(numbers[0:10])

main()



