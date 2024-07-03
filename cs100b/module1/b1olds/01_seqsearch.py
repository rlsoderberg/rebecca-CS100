#import random to generate randomized list
import random

#define selection search function that uses for loop to go through list to search
def sequential_search(needle, haystack):
    #for loop going through haystack and checking for needle at each location
    #len(haystack) - 1 is end of range, since haystack starts at 0
    print(len(haystack))
    #remember to include the word 'range', otherwise your program will just look at haystack[0] and haystack[-1]
    for x in range (0, len(haystack) - 1):
        if str(haystack[x]) == str(needle):
            return x
    #if loop has completed without finding needle, then return -1
    return -1


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

#define main function
def main():
    #initialize random string
    rand_string = ''
    #generate random letter string
    rand_string = random_string()
    print(f'random letter string: {rand_string}')

    #set search term
    search_term = 'q'

    #initialize location
    location = 0

    #execute selection search
    location = sequential_search(search_term, rand_string)

    if location == -1:
        print(f"couldn't find search term {search_term} in random letter string")
    else:
        print(f"found search term {search_term} at location {location}.")


main()



