#oh wait, there are multiple sets of 1s and 2s and 3s and 4s in this module
#i accidentally started with the second set?
#no, i have literally no idea what i am doing right now
from course import Course
from teacher import Teacher

def int_input_function():
    valid = False
    while valid == False:
        try:
            value = int(input())
            if value == '':
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print('Invalid Input')


teacher72 = Teacher('Hemingway', 203, 'English')
teacher73 = Teacher('Feynman', 166, 'Physics')
teacher74 = Teacher('Hypatia', 122, 'Philosophy')
teacherlist = [teacher72, teacher73, teacher74]

#i thought i was going to be outputting these in a loop? whatever that means?
for x in teacherlist:
    print(f'Name: {x.name} Office: {x.office} Department: {x.department}')
#but now i don't even know where i saw that question so idk i'll take another look at the questions?
#honestly, i think classes are fairly self-explanatory, so i'm not too worried about it
    