import sys
sys.path.append('../..')


from i import input_function 

import datetime

#classes
class Student:
    name = ''
    ID = -1
    favsport = ""
    birthdate = '1/1/2000'

class Teacher:
    name = ""
    office = 0
    hobby = ""
    birthdate = '1/1/2000'

class Course:
    name = ""
    classroom = 0
    teacher = ""
    students = []
#set class properties, and print
stud = Student
stud.name = "billy bob"
stud.ID = 19789291
stud.favsport = "golf"
stud.birthdate = '4/10/1991'
print("we wanted to throw a  "+stud.favsport+" party for "+stud.name+" on his birthday, "+stud.birthdate+", but we got intercepted by birthday gnomes, who were attracted to the number"+str(stud.ID))
teach = Teacher
teach.name = "mr giles"
teach.office = 202
teach.hobby = "cross-referencing"
teach.birthdate = '4/4/1944'
print("On "+str(teach.birthdate)+", we brought a birthday cake to the office of "+str(teach.name)+", room "+str(teach.office)+", but he was busy "+str(teach.hobby)+".")
algebra = Course
algebra.name = "Algebra"
algebra.classroom = 204
algebra.teacher = "mr. mcneil"
algebra.students = ["colleen fumpo", "paul leghat", "rachel stendec", "michael overgold", "ali redbuckle"]
print(algebra.name+" Roster\nTeacher: "+algebra.teacher+"\nStudents Beginning With M:")
#special loop of m
for s in algebra.students:
    if s.startswith('m'):
        print(s)


