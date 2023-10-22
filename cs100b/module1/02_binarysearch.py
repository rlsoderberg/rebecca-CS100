#import random to generate randomized list
import random

#define function to generate random number string
def number_list():
    list = []
    for x in range (0, 50):
        r = random.randrange(100)
        list.append(r)
    return list

def binary_search(haystack, needle):
    #keep track of begin and end as numbers, not as values on list
    begin = 0
    end = len(haystack)

    #while begin <= end keeps the search going as the searched area gets smaller and smaller
    while begin <= end:
        #flexible haystack length, with mobile midpoint & begin & end
        #use floor division to get an integer midpoint, which you can use as a list position
        midpoint = begin + (end - begin)//2
        #cut flexible length in half each time, setting midpoint as edge
        if haystack[midpoint] < needle:
            begin = midpoint + 1
        elif haystack[midpoint] > needle:
            end = midpoint - 1
        else:
        #binary search narrows all the way down to midpoint = needle, still faster than going one by one 
            return midpoint

    #if loop has completed without finding needle, then return -1
    return -1


#use number list function to generate list
list = number_list()
#sort list for binary search
list.sort()
print(f'sorted random string: {list}')
search_term = 59

#search list with binary search
location = binary_search(list, search_term)
#print results
if location == -1:
    print(f'did not find {search_term}')
else:
    print(f'found {search_term} at location {location}')














