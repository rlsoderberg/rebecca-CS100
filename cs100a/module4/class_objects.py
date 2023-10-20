#oh wait, there are multiple sets of 1s and 2s and 3s and 4s in this module
#i accidentally started with the second set?
#no, i have literally no idea what i am doing right now

#import random for extra bonus
import random

#ooh, i have been forgetting to document all of this stuff!
#import classes
from course import Course
from teacher import Teacher
from student import Student

#define int input function
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

#introduce teacher list
print('\nLIST OF TEACHERS:')
#create teacher objects
teacher72 = Teacher('Dickens', 203, 'English')
teacher73 = Teacher('Feynman', 166, 'Physics')
teacher74 = Teacher('Hypatia', 122, 'Astronomy')
#put teacher objects into teacher list
teacherlist = [teacher72, teacher73, teacher74]

#i thought i was going to be outputting these in a loop? whatever that means?
for x in teacherlist:
    print(f'Name: {x.name} Office: {x.office} Department: {x.department}')
#but now i don't even know where i saw that question so idk i'll take another look at the questions?
#honestly, i think classes are fairly self-explanatory, so i'm not too worried about it

#create student objects
student1 = Student()
#what is the best way to do this, if you skip the parentheses variables???
#LEGITIMATE QUESTION ALERT
student1.name = 'Plambo' 
student1.ID = 77704
student1.birthdate = '12/07/1942'

student2 = Student('Hyborg', 60378, '06/06/1973')

student3 = Student('Malfoy', 87423, '06/05/1980')

#put student objects into student list
studentlist = [student1, student2, student3]

#introduce student list
print('\nLIST OF STUDENTS *starting with m:')

#i will make the student roster with a while loop, just for funsies
"""while x in studentlist:
    print(f'Student Name: {x.name} Student ID: {x.ID} Student Birthdate: {x.birthdate}')"""
#well, THAT didn't work. apparently we can use len(list)?
"""while i > len(studentlist):
    print(f'Student Name: {x.name} Student ID: {x.ID} Student Birthdate: {x.birthdate}')
    i += 1"""
#hey, this isn't working!!! they say i is not defined!!!
#well, that's kind of annoying. maybe ask about mass initialization without parentheses, and while loop list
#the trusty for loop
for x in studentlist:
    #every student asks a question
    #bonus!!!
    #if x.name.startswith('M'): i got rid of the bonus because i did think it was nice that the names lined up
    print(f'Student Name: {x.name} Student ID: {x.ID} Student Birthdate: {x.birthdate}')
    
""" 
    at this point i am pretty dedicated to the names lining up. close proximity adds to the effect, i think.
    alas for behaviors...

    #extra bonus!!!
    rando = random.randint(1, 3)
    if rando == 1:
        x.study()
    elif rando == 2:
        x.do_homework("Loop")
    elif rando == 3:
        x.ask_question()
        #it is telling me that 'Student' object has no attribute 'ask_question'!!!
        #of course, it was indented wrong!!!!!!!"""








    