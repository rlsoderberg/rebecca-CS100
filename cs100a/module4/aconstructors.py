import random

#constructors
class Student():
    def __init__(self, name = "", ID = -1, birthdate = '1/1/2000'):
        self.name = name
        self.ID = ID
        self.birthdate = birthdate

    def study(self):
        print(self.name+" is studying.")

    def do_homework(self, course):
        print(self.name+" is doing "+course+" homework.")
    
    def ask_question(self):
        print("wait, what?")

stud = Student('moon',24924,'10/24/1973')
stud.study

class Teacher():

    def __init__(self, name = "", office = -1, birthdate = "1/1/2000"):
        self.name = name
        self.office = office
        self.birthdate = birthdate

    def cross_reference(self, subject):
        print(self.name+" is cross-referencing books about "+subject)

    def advertise(self, passion):
        print(self.name+" puts up a sign outside room "+str(self.office)+" for the Big Annual "+passion+" Festival.")

    def party(self):
        print(self.name+" is throwing a party with fellow staff members also born on "+self.birthdate)  

teacher1 = Teacher("mr. haggisford", 273, '2/20/1960')
#list of constructed variables
music_department = [Teacher("mrs. cromwell",166,'7/10/1952'),Teacher("mr. palmfob",172,'6/30/1958'),Teacher("ms. blisterall", 280,'8/28/1998'),Teacher("mr. bometta",102,'2/18/1971')]

print("Music Department Staff:")
for t in music_department:
    print("Name: "+t.name+"   Office: "+str(t.office))

class Course():
    def __init__(self, name = "", classroom = -1, students = []):
        self.name = name
        self.classroom = classroom
        self.students = students
    
    def secret_santa(self, object):
        print(self.students.first+" gives "+object+"to their secret santa, "+self.students.last)

    def roll_call(self):
        print("there are "+str(len(self.students))+" students absent today")
    
    def max_occupancy(self):
        print("maximum occupancy of room "+self.classroom+" is "+str(len(self.students)*10))

major_chemistry = [Course("biochemistry",111,["dwight","tabitha","mungo"]), Course("forensic chemicals", 125, ["priscilla", "dwight", "lamprey"]), Course("chemical analysis", 66, ["portia", "lamprey", "mungo"])]

print("requirements for a major in chemistry: ")
for c in major_chemistry:
    print("Course: "+c.name+"   Room: "+str(c.classroom)+"   Tutor: "+random.choice(c.students))