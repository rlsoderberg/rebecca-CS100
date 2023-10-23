class Person:
    #constructor with basic person information
    def __init__(self, name = '', birthdate = ''):
        self.name = name
        self.birthdate = birthdate

    #person behaviors
    def eat(self):
        print(f'{self.name} is eating.')

    def sleep(self):
        print(f'{self.name} is sleeping.')
    
    def introduction(self):
        print(f'hello, my name is {self.name}')
        