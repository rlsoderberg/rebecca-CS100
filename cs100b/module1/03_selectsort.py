#import random for random number list
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
        list[item] = ''
        list.split()
        list[min] = list[item]
        newlist = list[0] + list[min] + list[1]
        
    #return sorted list
    return newlist

#define function to generate random letter string
def random_string():
    #generate string containing all letters in alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #initialize string to put random letters in
    random_string = ''
    #initialize random character
    char = ''
    #for loop to generate a string of 26 random characters
    for x in range (0, 27):
        rando = random.randrange(len(alphabet))
        char = alphabet[rando]
        random_string = random_string + char
    return random_string

#random number list
list = random_string()
#sort list with selection sort function
sorted_list = selection_sort(list)
#display results
print(f'sorted list: {sorted_list}')