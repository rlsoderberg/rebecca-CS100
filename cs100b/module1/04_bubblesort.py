#import random to generate randomized list
import random

#define bubble sort function
def bubble_sort(list):
    #swap variable keeps us swapping until there is nothing left to swap
    swap = True
    while swap:
        #with each round of the while loop, we get another chance for peace, which can be broken by a swap
        swap = False
        #the for loop is where we go through and look for swaps
        #range(9, len(list)-1) allows x + 1 to always stay within range
        for i in range(0, len(list)-1):
            if list[i] > list[i+1]:
                #swap breaks the peace
                swap = True
                #switch the variables which are out of order
                #make sure you do the swap right, or else your sorted list will be heavy on repeated low variables
                tmp = list [i]
                list [i] = list [i+1]
                list[i+1] = tmp

def main():
    #generate random number list
    int_list = []
    for x in range(0, 50):
        int_list.append(random.randrange(0, 25))

    #sort list with selection sort function
    sorted_list = bubble_sort(int_list)

    #create alphabet string
    alphabet='abcdefghijklmnopqrstuvwxyz'
    #initialize char list
    char_list = []
    #convert num list to char list
    for x in range(0, len(int_list)):
        char_list.append(alphabet[int_list[x]])

    #display results
    print(f'sorted list: {char_list}')

main()
        