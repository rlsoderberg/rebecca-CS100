#1. 

import random

class Student:
    #so, i'm trying to remember... i'm used to initializing attributes up here, right?
    #and then assigning them to themselves in the body of the function?
    def __init__(self):
        """
        Create a default statement
        """
        self.name = ''
        self.id = -1
        self.birthdate = '1/1/2001'

class Teacher:
    def __init__(self):
        """
        Create a default statement
        """
        self.name = ''
        self.id = -1
        self.birthdate = '1/1/2001'

class Course:
    def __init__(self):
        """
        Create a default statement
        """
        self.name = ''
        self.id = -1
        self.teacher_id = -1



#create student object
#and if you initialize the attributes in init parenths, you can define them in these parenths here, can't you?
stud0 = Student()

#initialize student list
studlist = []

#change the student's properties
stud0.name = 'Mary'
stud0.id = '12345'
stud0.birthdate = '1/1/1999'
studlist.append(stud0)

#2. when you print the student name, the name of student Mary is printed
#print(stud.name)


#3.
#print(stud.id, stud.birthdate)

#create two more student objects
stud1 = Student()

stud1.name = 'Jerry'
stud1.id = 12346
stud1.birthdate = '1/1/1999'
studlist.append(stud1)

stud2 = Student()

stud2.name = 'Carey'
stud2.id = 12347
stud2.birthdate = '1/1/1999'
studlist.append(stud2)

#print student objects
print('list of students:')
for s in studlist:
    #oh, make sure to write s.name, or else it will print Mary three times...
    #and this should probably be the first spot you check, since this is where the error is coming from
    print(s.name)

#1. 

#initialize teacher list
teachlist = []

#create teacher object
#you have to put the class at the top of the page, or else this doesn't work!
teach0 = Teacher()

teach0.name = 'Boris'
teach0.id = 57426
teach0.birthdate = '4/4/1944'
teachlist.append(teach0)

#2.

course0 = Course()

course0.name = 'Phlebotomy 101'
course0.id = 64533
course0.teacher_id = 57426

for t in teachlist:
    print(f'teacher name is {t.name}' )
    if(t.id == course0.teacher_id):
        #remember to put the f in the f string
        print(f'{t.name} is teaching {course0.name}')

#3.

#initialize student list
students = []

#list of names
namepile = ['Maeve', 'Mahabala', 'Mary', 'Mathrudev', 'Meghan', 'Meru', 'Moira']
#list of students


#create student objects
stud01 = Student()
stud02 = Student()
stud03 = Student()
stud04 = Student()
stud05 = Student()
#'extend' students to student list. here's those double parentheses, there must be a better way to do this...
students.extend((stud01, stud02, stud03, stud04, stud05))

#i'm using my enumerator to make a list of students with random names
#look, is enumerate even the best way to do this? it sure is an easy shortcut...
for index, s in enumerate(students, start = 1):
    s.name = namepile[random.randrange(len(namepile))]
    #oh, THIS is a better way to prevent duplicates, you remove after using...
    namepile.remove(s.name)
    if s.name.startswith('M'):
        print(f'student {index}: {s.name}')

#4. print only students with name starting m







