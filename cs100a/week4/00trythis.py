class Student:
    name = ''
    ID = -1
    birthdate = '1/1/2000'


stud01 = Student()
stud01.name = 'Mary'
stud01.ID = 10101
stud01.birthdate = '1/1/1999'

#1. LOOKS OK TO ME...

#2. <__main__.Student object at 0x00000200D4348BE0>

print("3. ",vars(stud01),"\n")


studentlist = []
studentlist.append(stud01)


stud02 = Student()
stud02.name = 'Rocky'
stud02.ID = 63932
stud02.birthdate = '11/19/1959'
studentlist.append(stud02)

stud03 = Student()
stud03.name = 'Bullwinkle'
stud03.ID = 93018
stud03.birthdate = '06/27/1954'
studentlist.append(stud03)

for number, element in enumerate(studentlist, 1):
    print("Student ",number,": ",vars(element))
