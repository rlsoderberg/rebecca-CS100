class Student:
    name = ''
    ID = -1
    grade = '1/1/2000'


stud01 = Student()
stud01.name = 'Mary'
stud01.ID = 10101
stud01.grade = 3.5

print("3. ",vars(stud01),"\n")


studentlist = []
studentlist.append(stud01)


stud02 = Student()
stud02.name = 'Rocky'
stud02.ID = 63932
stud02.grade = 2.6
studentlist.append(stud02)

stud03 = Student()
stud03.name = 'Bullwinkle'
stud03.ID = 93018
stud03.grade = 4.2
studentlist.append(stud03)

stud04 = Student()
stud04.name = 'Maxwella'
stud04.ID = 97426
stud04.grade = 3.3
studentlist.append(stud04)

stud05 = Student()
stud05.name = 'Jimbob'
stud05.ID = 63271
stud05.grade = 1.2
studentlist.append(stud05)

print("Names starting with M: ")
for c in studentlist:
#    print("Name: ",c.name," ID: ",c.ID," Grade: ",c.grade,"\n")
    #4
    sample_str = c.name
    if sample_str[0] == 'M':
        print("Name: ",c.name," ID: ",c.ID," Grade: ",c.grade)
