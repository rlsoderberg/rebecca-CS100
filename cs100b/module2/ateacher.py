class Person:
    def __init__(self, name = "", age = -1, birthdate = '1/1/2000'):
        self.name = name
        self.age = age
        self.birthdate = birthdate
    def eat(food):
        print("this "+food+" is tasty")
    def sleep():
        print(self.name + "is asleep")

class Course:
    def __init__(self, title = "", students = [], projects = []):
        self.title = title
        self.students = students
        self.projects = projects

class Project:
    def __init__(self, name):
        self.name = name

class Food:
    def __init__(self, name):
        self.name = name

class Teacher (Person):
    def teach(course):
        print(self.name + " is teaching " + course.name)
    def grade(course):
        print(self.name + "is grading " + course.projects[-1])

class Student(Person):
    def study(course):
        print((self.name) + "is studying")

def main():

    sam = Teacher("Samuel Woolsworth")
    zeppo = Student("Zeppo Marx")
    tammy = Student("Tamara Roberts")
    tammy.name = Student("Tamara Roberts")
    eliza = Student("Eliza Elaza")

    polyrap = Project("Rap about Polynomials")
    fractalcooking = Project("Fractal Cooking Challenge")

    math101 = Course("Introduction to Geometry")
    math101.student = [zeppo, tammy, eliza]
    math101.project = [polyrap, fractalcooking]

    mango = Food("Mango")

    sam.teach(math101)
    sam.grade(math101)

if __name__ == '__main__':
    main()
    