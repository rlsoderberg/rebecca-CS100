"""
LOOK, THIS WHOLE THING ISN'T WORKING

#here, i'm trying to do this without looking, let's see how it goes

def sequentialsearch(haystack, searchterm): #forgot arguments
    for i in range(0, len(haystack)): #still not sure why i have to do it this way
        if(haystack[i] == searchterm): #forgot parentheses OH, haystack[i] was key!!!!!!!!!!!!!!!!!!!!!
            return i

    return -1  

searchterm = input("enter a number between 1 and 10: ")
haystack = [3,5,6,7,2,4,9]

position = sequentialsearch(haystack, searchterm)


if position == -1:
    print(f"{searchterm} is not in the haystack")
else:
    print(f"i found {searchterm} at position {position}.")

"""

#SEQUENTIAL SEARCH
#sequential search, you go through the whole haystack, one hay at a time

import random

def sequentialsearch(haystack, needle):
    for i in range(0, len(haystack)):
        if (haystack[i] == needle):
            return i

    return -1

#BINARY SEARCH
#start in the middle, see if it's higher or lower (data needs to be sorted)
"""
WHY WASN'T THIS WORKING???????
def binarysearch(haystack, needle):

    haystack.sort() #can i just put the sort up here for this one?

    start = 0           #you keep track of the start and the end!!!
    end = len(haystack)

    #oh, i'm just stealing this whole thing! i can never remember how to do this! 
    #maybe i will steal it today and then see if i can remember it tomorrow?

    while start <= end:
        i = start + (end - start)//2 #why are there two slashes???
        if haystack[i] < needle:
            start = i + 1
        elif haystack[i] < needle:
            end = i - 1
        else: return i
        #oh i get it, it turns itself into the beginning or end which is how it cuts itself in half
        #and then it starts by going halfway through

    return -1

#wait, it did sort numbers, and i don't really get how? how much stuff do you have to return in python?
"""
def binarysearch(haystack, needle):

    haystack.sort()

    start = 0
    end = len(haystack)

    while start <= end:
        i = start + (end-start)//2
        if haystack[i] < needle:
            start = i+1
        elif haystack[i] > needle:
            end = i-1
        else:
            return i

    #if we're out of the loop, we didn't find it
    return -1

#SELECTION SORT
#you start with the start of your list as your min, and then you switch if you find something smaller
"""
def selectionsort(haystack, needle):
    for i in range(0, len(haystack)):
        min = i

        for j in range (i, len(haystack)):
            if haystack[j] < haystack[min]:
                min = j

        tmp = haystack[i]
        haystack[i] = haystack[min]
        haystack[min] = tmp

        return -1
    
    #with selection sort, you go number by number, so you use tmp to hold if you switch it, and then...
    #and then, like, you have the min, but you still keep going???
    #right, so yeah, we're not returning anything. is that just how, like, it works?
"""
#this one isn't working either???

def selectionsort(haystack):
    for i in range(0, len(haystack)):
        min = i
        #look for an item smaller than list[min]
        for j in range(i, len(haystack)):
            if haystack[j] < haystack[min]:
                min = j     #just remember where this was
        #we've found it. Swap it into this location
        tmp = haystack[i]
        haystack[i]=haystack[min]
        haystack[min] = tmp

#BUBBLE SORT
#you just loop through the list multiple times, and switch if the one on the right is bigger?
"""
def bubblesort(haystack, needle):
    swap = True #i am honestly not entirely sure what this is for?
    while swap: #ohhh this is what it is for, so you loop until you don't need to swap anywhere
        swap = False
        for i in range (0, len(haystack) - 1):
            if haystack[i] < haystack[i + 1]:
                swap = True
                tmp = haystack[i]
                haystack [i] = haystack [i+1]
                haystack[i+1] = tmp #i was able to execute the switch from memory, at least, hahaha

    return -1
"""
def bubblesort(haystack): #it seems to like it better when i use var haystack instead of list in the sorts????
    swap = True
    while swap:
        swap = False
        for i in range(0, len(haystack)-1):
            if haystack[i] > haystack[i+1]:
                swap = True
                tmp = haystack[i]
                haystack[i] = haystack[i+1]
                haystack[i+1] = tmp

#INSERTION SORT
#move things around to make room

def insertionsort(haystack):
    for i in range(1, len(haystack)):
        number = haystack[i] #so number is your tmp, basically???
        pos = i 
        while pos > 0 and haystack[pos - 1] > number: #rearrange all the way back, as long as you can
            haystack [pos] = haystack [pos - 1]
            pos = pos - 1 
        haystack[pos] = number

def main(variable):
    while variable == '':
        numbers = list = [3,5,6,7,2,4,9]
        print(f"number list: {numbers}")

        target = int(input("enter a number between 1 and 10: "))

        type = "X"
        type = input("do you want to do:\nA) a sequential search\nB) a binary search\nC) a selection sort \nD) a bubble sort \nE) an insertion sort ?")

        while type != "A" and type != "B" and type != "C" and type != "D" and type != "E":
            type = input("invalid input. do you want to do:\nA) a sequential search\nB) a binary search\nC) a selection sort \nD) a bubble sort \bE) an insertion sort ?")
        if type == "A":
            location = sequentialsearch(numbers, target)
        elif type == "B":
            location = binarysearch(numbers, target)
        elif type == "C":
            location = selectionsort(list)
        elif type == "D":
            location = bubblesort(list)
        elif type == "E":
            location = insertionsort(list) #why doesn't it like when i insertionsort(numbers)??????
        if type == "A" or type == "B":
            print(f"new number list: {numbers}")
            if location == -1:
                print(f"\ncouldn't find {str(target)} in number list")
            else:
                print("found " + str(target) + " at location " + str(location))
        elif type == "C" or type == "D" or type == "E":
            print(f"new number list: {list}")


        variable = input ("press enter to start over or x to exit ")


variable = ''
main(variable)
    