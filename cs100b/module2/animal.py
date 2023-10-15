#import parent class
from eukaryote import Eukaryote

class Animal(Eukaryote):
    def __init__(self, name = '', species='', kingdom='', cellularity='', feeding='', reproduction=''):
        self.name = name
        self.species = species
        self.kingdom = kingdom
        self.cellularity = cellularity
        self.feeding = feeding
        self.reproduction = reproduction

#class behaviors
    def sleep(self):
        print(f"the {self.name} habitually becomes dormant for periods of its lifecycle.")

    def learn_behavior(self, behavior):
        print(f'the {behavior} behavior of the {self.name} is shaped by the lived experience of the {self.name}')
    
    def directional_movement(self):
        print(f'the {self.name} performs directional movements, such as thermoregulation.')  