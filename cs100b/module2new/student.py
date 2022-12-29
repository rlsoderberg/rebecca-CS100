from person import Person

class Student(Person):
    def __init__(self, name, ID=0,birthdate='1/1/2000'):
        Person.__init__(self, name, ID, birthdate)