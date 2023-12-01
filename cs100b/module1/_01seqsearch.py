#oh here's the module with all the algorithms!!!
import random
#you always need a haystack and a neeedle
def sequential_search(haystack, needle):
    for i in range(0, len(haystack)):
        if haystack[i] == needle:
            return i
    #return -1 if not found   
    return -1

#this string search is totally not working!!! so i'm separating it into smaller functions...
def short_string(l):
    letters = 'abcdefghijklmopqrstuvwxyz'
    length = l
    s = ''
    for c in range(0,length):
        i = random.randrange(0,len(letters))
        s = s + letters[i]
    return s

def write_strings(strings):
    f = open('randomstrings.txt', 'w')
    for x in range(0, len(strings)):
        #using join to add newlines
        f.write('\n' + str(x))
        f.write('\n')
    f.close()

def main():
    string_list = []
    #r controls size of string list
    #higher r makes you more likely to find target
    r = 6000
    #l controls length of strings
    #lower l makes you more likely to find target
    l = 3

    #loop to create string list
    for x in range(0, r):
        s = short_string(l)
        string_list.append(s)

    write_strings(string_list)

    target = short_string(l)

    location = sequential_search(string_list, target)

    #well, i think it's been working for a while, but it just it doesn't find very often
    #it was a combination of small things...
    #don't use join because +ing strings works fine
    #maybe use 'for x in strings' instead of using range, although i'm not entirely sure when each is better
    #finally, use target down here instead of str(s)
    #now, let me make it so i can mess about with probability
    if location == -1:
        print(f"couldn't find {target}")
    else:
        print(f'found {target} at {str(location)}')

main()

