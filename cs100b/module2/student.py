#import person base class
from person import Person

class Student(Person):
    #constructor with basic person information as well as student-specific information like grade level
    def __init__(self, name = '', ID = 0, birthdate = '', grade_level = 0):
        self.name = name
        self.ID = ID
        self.birthdate = birthdate
        self.grade_level = grade_level

    #student behaviors
    def ask_question(self):
        print('wait, what?')

    def do_homework(self):
        print(f'{self.name} is doing homework.')

    def study(self):
        print(f'{self.name} is studying.')

    #student version of person behavior introduction
    def introduction(self):
        print(f'yo, my name is {self.name}')