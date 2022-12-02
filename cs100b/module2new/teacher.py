from person import Person

class Teacher(Person):
    def __init__(self, name, ID=-1,birthdate='1/1/2000'):
        Person.__init__(self, name, ID, birthdate)

