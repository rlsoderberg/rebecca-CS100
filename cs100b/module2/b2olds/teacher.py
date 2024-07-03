from person import Person

#teacher class inherits from person class
class Teacher(Person):
    def __init__(self, name = '', id = -1, birthdate = '1/1/1999'):
        self.name = name
        self.id = id
        self.birthdate = birthdate

    def teach(self):
        print(f'{self.name} is teaching')

    def assign_homework(self, course):
        print(f'{self.name} assigned homework in {course} course')

    def answer_question(self):
        print(f'Let me see if I can help')

#introduction is polymorphic behavior
    def introduction (self):
        print(f'good morning, my name is professor {self.name}')