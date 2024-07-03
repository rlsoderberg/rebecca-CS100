#person is base class for student, teacher, and busdriver
class Person:
    def __init__(self, name = '', id = -1, birthdate = '1/1/1999'):
        self.name = name
        self.id = id
        self.birthdate = birthdate

    def eat(self):
        print('Yum')

    def sleep(self):
        print('Snore')

    def introduction(self):
        print(f'Hello, my name is {self.name}')





    