import sys
sys.path.append('../..')


from i import input_function 

import datetime

class Teacher:
    name = ""
    office = ""
    hobby = ""
    birthdate = 1/1/2000

print("which problem would you like to view? 1. teacher, 2. course, 3. roster, or 4. M ?")

problem = ""

while problem != "1" and problem != "2" and problem != "3" and problem != "4":
    problem = input()

if problem == "1":
    teach = Teacher
    teach.name = "mr giles"
    teach.office = "lib 202"
    teach.hobby = "cross-referencing"
    teach.birthdate = 4/4/1944
    print("On "+str(teach.birthdate)+", we brought a birthday cake to the office of "+str(teach.name)+", "+str(teach.office)+", but he was busy "+str(teach.hobby)+".")
