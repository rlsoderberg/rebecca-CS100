#function for select sort
def selection_sort(list):
    for x in range(0, len(list)):
        min = x
        for s in range(x, len(list)):
            if list[s] < min:
                min = s
        tmp = list[s]
        list[s] = list[min]
        list[min] = tmp 

    return list

"""
874509
min = 8
s = 1 7 is smaller than 8 min = 7
s = 2 4 is smaller than 7 min = 4
s = 4 0 is smaller than 4 min = 0
8 and 0 switch places
074589
min = 7
s = 1 4 is smaller than 7 min = 4
7 and 4 switch places
047589
min = 7
s = 1 5 is smaller than 7 min = 5
7 and 5 switch places
045789

093354
min = 0
093354
min = 9
s = 1 3 is smaller than 9 min = 3
9 and 3 switch places
039354
min = 9
s = 1 3 is smaller than 9 min = 3
9 and 3 switch places
033954
min = 9
s = 1 5 is smaller than 9 min = 5
s = 2 4 is smaller than 5 min = 4
9 and 4 switch places
033459

372432
min = 3
s = 2 2 is smaller than 3 min = 2
3 and 2 switch places
273432
min = 7 
s = 1 3 is smaller than 7 min = 3
s = 4 2 is smaller than 3 min = 2
7 and 2 switch places
223437
min = 3
223437
min = 4
s = 1 3 is smaller than 4 min = 3
4 and 3 switch places
223347

0.0973520937634
min = 0
1.0973520937634
min = 9
s = 1 7 is smaller than 9 min = 7
s = 2 3 is smaller than 7 min = 3
s = 4 2 is smaller than 3 min = 2
s = 5 0 is smaller than 2 min = 0
9 and 0 switch places
2.0073529937634
min = 7
s = 1 3 is smaller than 7 min = 3
s = 3 2 is smaller than 3 min = 2
7 and 2 switch places
3.0023579937634
min = 3
4.0023579937634
min = 5
s = 4 3 is smaller than 5 min = 3
5 and 3 switch places
5.0023379957634
min = 7
s = 3 5 is smaller than 7 min = 5
s = 6 3 is smaller than 5 min = 3
7 and 3 switch places
6.0023339957674
min = 9
s = 2 5 is smaller than 9 min = 5
s = 6 4 is smaller than 5 min = 4
9 and 4 switch places
7.002334957679
min = 9
s = 1 5 is smaller than 9 min = 5
9 and 5 switch places
8.002334597679
min = 9 
s = 1 7 is smaller than 9 min = 7
s = 2 6 is smaller than 7 min = 6
9 and 6 switch places
9.002334567979
min = 7
10.002334567979
min = 9
s = 1 7 is smaller than 9 min = 7
9 and 7 switch places
11.002334567799

0.303562
min = 3
s = 1 0 is smaller than 3 min = 0
3 and 0 switch places
1.033562
min = 3
s = 4 2 is smaller than 3 min = 2
3 and 2 switch places
2.023563
min = 3
3.023563
min = 5
s = 2 3 is smaller than 5 min = 3
5 and 3 switch places
4.023365
min = 6
s = 1 5 is smaller than 6 min = 5
6 and 5 switch places
5.023356










"""


list = [8, 7, 4, 5, 0, 9]
sort_list = selection_sort(list)
print(f'sorted list: {sort_list}')