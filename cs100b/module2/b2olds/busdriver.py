from person import Person

#busdriver class inherits from person class
class Busdriver(Person):
    def __init__(self, name = '', id = -1, birthdate = '1/1/1999'):
        self.name = name
        self.id = id
        self.birthdate = birthdate

    def turn_signal(self, direction):
        print(f'{self.name} turns on the {direction} turn signal')

    def pull_over(self):
        print(f'{self.name} pulls over to drop off some students')

    def school_zone(self):
        print(f'{self.name} slows down for the school zone')

#intoduction is polymorphic behavior
    def introduction(self):
        print(f"all aboard! you can call me captain {self.name}")