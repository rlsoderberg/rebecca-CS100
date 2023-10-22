#define bubble sort function
def bubble_sort(list):
    #swap variable keeps us swapping until there is nothing left to swap
    swap = True
    while swap:
        #with each round of the while loop, we get another chance for peace, which can be broken by a swap
        swap = False
        #the for loop is where we go through and look for swaps
        for x in range(0, len(list)):
            if list[x] > list[x+1]:
                #swap breaks the peace
                swap = True
                #switch the variables which are out of order
                tmp = list [x+1]
                list [x] = list [x+1]
                list[x+1] = tmp


        