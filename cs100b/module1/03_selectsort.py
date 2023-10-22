#import random to generate randomized list
import random

#function for select sort
def selection_sort(list):
    #loop through each item in list 
    for item in range(0, len(list)):
        #first for loop runs through the list, one list position at a time
        #we mark the new list item as min, and look for a value that's even lower
        min = item
        #second for loop runs through list values following item, looking for a lower value
        for l in range(item, len(list)):   
            #when we find a lower value, min becomes l, so we can keep looking for the lowest value to swap with item    
            if list[l] < list[min]:
                min = l
        #now that we have gone through the second loop, and we have found the lowest value to swap with item
        #we swap the lowest value with item
        tmp = list[item]
        list[item] = list[min]
        list[min] = tmp

    #return sorted list
    return list

#define function to generate random number string
def number_list():
    list = []
    for x in range (0, 50):
        r = random.randrange(100)
        list.append(r)
    return list

#generate random number list
list = number_list()
#sort list with selection sort function
sorted_list = selection_sort(list)
#display results
print(f'sorted list: {sorted_list}')