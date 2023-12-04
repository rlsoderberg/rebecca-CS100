from person import Person

#student class inherits from person class
class Student(Person):
    def __init__(self, name = '', id = -1, birthdate = '1/1/1999', gradelevel = 0):
        self.name = name
        self.id = id
        self.birthdate = birthdate
        self.gradelevel = gradelevel

    def study(self):
        print(f'{self.name} is studying')

    def do_homework(self, course):
        print(f'{self.name} is doing their {course} homework')
              
    def ask_question(self):
        print('Wait, what?')

#introduction is polymorphic behavior
    def introduction(self):
        print(f'yo my name is {self.name}')