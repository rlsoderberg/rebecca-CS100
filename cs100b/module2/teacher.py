#import person base class
from person import Person

class Teacher(Person):
    #constructor with basic person information as well as teacher-specific information like ID
    def __init__(self, name = '', ID = 0, birthdate = ''):
        self.name = name
        self.ID = ID
        self.birthdate = birthdate

    #teacher behavior
    def teach(self):
        print(f'{self.name} is teaching.')

    def assign_homework(self):
        print(f'{self.name} assigned homework.')

    def answer_question(self):
        print('Let me see if I can help.')

    #teacher version of person behavior introduction
    def introduce(self):
        print(f'Good morning, my name is {self.name}')
