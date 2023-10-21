#import random to pick random function
import random

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

#display all teachers, with their characteristics, which do you not have to unpack, because they are class objects
for x in teacherlist:
    print(f'Name: {x.name} Office: {x.office} Department: {x.department}')

#create student objects
student1 = Student()

#assign student characteristics
student1.name = 'Plambo' 
student1.ID = 77704
student1.birthdate = '12/07/1942'

#assign student characteristics, the really smooth way
student2 = Student('Hyborg', 60378, '06/06/1973')

student3 = Student('Malfoy', 87423, '06/05/1980')

#put student objects into student list
studentlist = [student1, student2, student3]

#introduce student list
print('\nLIST OF STUDENTS:')

#for loop displaying students & student behaviors
for x in studentlist:
    print(f'Student Name: {x.name} Student ID: {x.ID} Student Birthdate: {x.birthdate}')
    #select random number
    rando = random.randint(1, 3)
    #choose which student behavior to execute, depending on random number
    if rando == 1:
        x.study()
    elif rando == 2:
        x.do_homework("Loop")
    elif rando == 3:
        x.ask_question()









    