class Teacher:
    name = ''
    officenumber = -1
    birthdate = '1/1/1925'


teach01 = Teacher()
teach01.name = 'Mrs. Pringles'
teach01.officenumber = 106
teach01.birthdate = '1/1/1975'

print("3. ",vars(teach01),"\n")


teacherlist = []
teacherlist.append(teach01)


teach02 = Teacher()
teach02.name = 'Miss Fudgesicle'
teach02.officenumber = 307
teach02.birthdate = '07/22/1939'
teacherlist.append(teach02)

teach03 = Teacher()
teach03.name = 'Mr. Asparagus'
teach03.officenumber = 225
teach03.birthdate = '12/05/1904'
teacherlist.append(teach03)

for number, element in enumerate(teacherlist, 1):
    print("Teacher ",number,": ",vars(element))
