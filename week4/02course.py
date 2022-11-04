class Course:
    name = ''
    classroomnumber = -1
    credits = 0


teach01 = Course()
teach01.name = "Anthropology"
teach01.classroomnumber = 106
teach01.credits = 5

print("3. ",vars(teach01),"\n")


courselist = []
courselist.append(teach01)


teach02 = Course()
teach02.name = "Knitting"
teach02.classroomnumber = 307
teach02.credits = 3
courselist.append(teach02)

teach03 = Course()
teach03.name = 'Water Polo'
teach03.classroomnumber = 225
teach03.credits = 2
courselist.append(teach03)

for number, element in enumerate(courselist, 1):
    print("Course ",number,": ",vars(element))
