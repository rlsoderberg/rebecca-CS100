#2.1

class Person:

    def __init__(self, name='', ID=-1, birthdate='1/1/2000'):
        self.name = name
        self.ID = ID
        self.birthdate = birthdate

    def eat(self):
        print('Mmmm, dinner')

    def sleep(self):
        print('snore')

    def introduction(self):
        print('hello my name is'+self.name)




