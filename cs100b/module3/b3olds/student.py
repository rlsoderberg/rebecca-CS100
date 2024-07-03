#student class for use in dictionary. this student, however, is not a person

#student class does not inherit from person class
class Student():
    def __init__(self, id = -1, name = '', birthdate = '1/1/1999', gradelevel = 0):
        self.name = name
        self.id = id
        self.birthdate = birthdate
        self.gradelevel = gradelevel

    def study(self):
        print(f'{self.name} is studying')

    def do_homework(self, course):
        print(f'{self.name} is doing their {course} homework')
              
    def ask_question(self):
        print('Bzzzt')

    def introduction(self):
        print(f'I am student number {self.id}')