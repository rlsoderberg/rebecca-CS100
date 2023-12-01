#1.

import random

class Student:
    #default statement
    def __init__(self, name = '', id = -1, birthdate = '1/1/2001'):
        """
        Create a default statement
        """
        self.name = name
        self.id = id
        self.birthdate = birthdate

    #study behavior
    def study(self):
        """
        Time to study
        """
        print(f'{self.name} is studying')

    #do homework behavior, taking course parameter
    def do_homework(self, course):
        """
        Time to do homework
            Parameters: course(str): the course to do the homework for
        """
        print(f'{self.name} is doing homework for their {course} course')

    #ask question behavior
    def ask_question(self):
        """
        Time to ask questions
        """
        print(f'What?')

class Teacher():
    def __init__(self, name = '', id = -1, birthdate = '1/1/1915'):
        self.name = name
        self.id = id
        self.birthdate = birthdate

    def erase_board(self):
        print(f'{self.name} is erasing the board')

    def give_lecture(self, course):
        print(f'{self.name} is giving a lecture in the {course} course')

    def grade_homework(self, student_name):
        print(f'{self.name} is grading the homework of {student_name}')

class Course():
    def __init__(self, name = '', id = -1, teacher_id = -1):
        self.name = name
        self.id = id
        self.teacher_id = teacher_id

    def is_full(self):
        print(f'{self.name} is full')

    def advising_week(self):
        print(f'{self.name} is letting out early for advising week')
    
    def required(self, reqs):
        print(f'Majors where this course is required: {reqs}')

stud = Student()

stud2 = Student('rambo', 1400, '2/4/1968')

print(stud.name)

#don't forget the parentheses!!!
stud2.do_homework('debate')
stud2.study()
stud2.ask_question()

#initialize object lists
teacher_objects = []
course_objects = []

#lists of teacher names & course names
teachs = ["mr. stauffer", "mrs. hannigan", "mr. polichek", "mrs. canembury"]
courses = ['roller skating', 'baking', 'ethics', 'communication']

teach01 = Teacher()
teach02 = Teacher()
teach03 = Teacher()
teach04 = Teacher()
teacher_objects.extend((teach01, teach02, teach03, teach04))
courses01 = Course()
courses02 = Course()
courses03 = Course()
courses04 = Course()
course_objects.extend((courses01, courses02, courses03, courses04))

#loop of teachers
for t in teacher_objects:
    t.name = teachs[random.randrange(len(teachs))]
    teachs.remove(t.name)
    rando = random.randrange(0, 3)
    if rando == 0:
        print('\nt rand = 0')
        t.erase_board()
    elif rando == 1:
        print('\nt rand = 1')
        t.give_lecture("self-defense")
    elif rando == 2:
        print('\nt rand = 2')
        t.grade_homework("Lisa Blamfort")

#loop of courses
for c in course_objects:
    c.name = courses[random.randrange(len(courses))]
    courses.remove(c.name)
    rando = random.randrange(0, 3)
    #you know, sometimes it tweaks out like '<__main__.Course object at 0x00000202941A3050> is full' and idk
    #ok, well, i'd better figure this out
    #i'm pretty sure this c0 the only one giving me trouble
    #well, i just rewrote it like this, and now it's working

    """

        def is_full(self):

        print(f'{self.name} is full')

    """
    #ohhhh, i was printing {self} is full
    if rando == 0:
        print('\nc rand = 0')
        c.is_full()
    elif rando == 1:
        print('\nc rand = 1')
        c.advising_week()
    elif rando == 2:
        print('\nc rand = 2')
        c.required(('knitting', "sewing"))
