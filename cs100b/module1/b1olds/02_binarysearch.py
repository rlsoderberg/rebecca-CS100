import random

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

#generate int list, char list, sort & search
def main():
    #generate list of random numbers 0-25, to be later converted into character string
    int_list = []
    for i in range(0, 40):
        int_list.append(random.randrange(0,25))
    #sort numbers for binary search
    int_list.sort()

    #create alphabet string
    alphabet='abcdefghijklmnopqrstuvwxyz'
    #initialize char list
    char_list = []
    #convert num list to char list
    for x in range(0, len(int_list)):
        char_list.append(alphabet[int_list[x]])

    #display char list in sorted order
    print(f'sorted random string: {char_list}')

    #generate random search term
    search_term = random.randrange(0,25)
    #search list with binary search
    location = binary_search(int_list, search_term)

        
    #print results
    if location == -1:
        print(f'did not find {alphabet[search_term]}')
    else:
        print(f'found {alphabet[search_term]} at location {location}')

#don't forget to run main
main()














