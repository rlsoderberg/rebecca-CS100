class Student:
    name = ""
    ID = -1
    birthdate = '1/1/2000'

    def study(self):
        print(self.name+" is studying.")

    def do_homework(self, course):
        print(self.name+" is doing "+course+" homework.")
    
    def ask_question(self):
        print("wait, what?")

stud = Student()
stud.name = "mary"
stud.ID = 42
stud.birthdate = "7/7/1942"

stud.do_homework("history")


class Teacher:
    name = ""
    office = -1
    birthdate = "1/1/2000"

    def cross_reference(self, subject):
        print(self.name+" is cross-referencing books about "+subject)

    def advertise(self, passion):
        print(self.name+" puts up a sign outside room "+str(self.office)+" for the Big Annual "+passion+" Festival.")

    def party(self):
        print(self.name+" is throwing a party with fellow staff members also born on "+self.birthdate)

teach = Teacher()
teach.name = "Fredby Glomworth"
teach.office = 523
teach.birthdate = '2/22/1999'

teach.advertise("Molerat")

class Course:
    name = ""
    classroom = -1
    students = []

    def secret_santa(self, object):
        print(self.students.first+" gives "+object+"to their secret santa, "+self.students.last)

    def roll_call(self):
        print("there are "+str(len(self.students))+" students absent today")
    
    def max_occupancy(self):
        print("maximum occupancy of room "+self.classroom+" is "+str(len(self.students)*10))

english = Course()
english.name = "Writing"
english.classroom="108"
english.students = ["marge", "bob", "henry", "krista", "kelsey"]

english.roll_call()


