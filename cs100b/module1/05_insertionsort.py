#import random to generate randomized list
import random

def insertion_sort(list):
    for i in range(1, len(list)):
        pos = i
        number = list[i]
        while pos > 0 and list[pos - 1] > number:
            list[pos] = list[pos - 1]
            pos = pos - 1
        list[pos] = number
"""
0.45034238
i = 0
pos = 0
number = list[0] = 4
pos !> 0 (skip)
1.45034238
i = 1
pos = 1
number = list[1] = 5
list[pos - 1] = 4, 4!> 5 
2.45034238
i = 2
pos = 2
number = list[i] = 0
-list[pos - 1] = 5, 5>0
list[pos] = list[pos - 1]: list[2] = 5
pos = pos - 1: pos = 1
-list[pos-1] = 4, 4>0
list[1] = 4
pos = 0
3.04534238
i = 3
pos = 3
number = 3
-list[pos - 1] = 5, 5>3
list[3] = 5
pos = 2
-list[pos - 1] = 4, 4>3
list[2] = 4
pos = 1
-list[pos - 1] = 0, 0!> 3
4.03454238
i = 4 
pos = 4
number = 4
-list[3]=5, 5>4
list[4]=5
pos = 3
-list[2]=4, 4!>5
without list[opos]=number:03455238
with list[opos]=number:03454238
5without.03455238
i = 5
pos = 5
number = 2
-list[4]=5, 5>2
list[5]=5
pos = 4
-list[3]=5, 5!>5
without: 034555...
5.03454238
i = 5 
pos = 5
number = 2
-list[4]=4, 4>2
list[5]=4
pos = 4
-list[3]=5, 5>2

0.35930546
i =0
pos =0
number = list[i] =3
while pos > 0 and list[pos - 1] > number:no
list[pos] = list[pos - 1] = 
pos = pos - 1 =
    list[pos] = number
1.35930546
i =1
pos =1
number = list[i] =5
while pos > 0 and list[pos - 1] > number:no
list[pos] = list[pos - 1] = 
pos = pos - 1 =
    list[pos] = number
2.35930546
i =2
pos =2
number = list[i] =9
while pos > 0 and list[pos - 1] > number:no
list[pos] = list[pos - 1] = 
pos = pos - 1 =
    list[pos] = number
3.35930546
i =3
pos =3
number = list[i] =3
while pos > 0 and list[pos - 1] > number:yes
list[3] = 9
pos = pos - 1 =2
while pos > 0 and list[pos - 1] > number:yes
list[2] = 5
pos = pos - 1 =1
while pos > 0 and list[pos - 1] > number:no
list[2] =
pos = pos - 1 =
    list[pos] = number

???

"""

#define function to generate random number string
def number_list():
    list = []
    for x in range (0, 50):
        r = random.randrange(100)
        list.append(r)
    return list

#generate random number list
list = number_list()
#sort list with insertion sort function
insertion_sort(list)
#display results
print(f'sorted list: {list}')