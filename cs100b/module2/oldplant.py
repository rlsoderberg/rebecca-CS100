from eukaryote import Eukaryote

class Plant(Eukaryote):
    def __init__(self, name = '', species='', kingdom='', cellularity='', feeding='', reproduction=''):
        self.name = name
        self.species = species
        self.kingdom = kingdom
        self.cellularity = cellularity
        self.feeding = feeding
        self.reproduction = reproduction

    def thigmotropism(self, stimulus):
        print(f"the {self.name} is touched by a {stimulus}, and the {self.name}'s leaves fold in response.")

    def photosynthesis(self):
        print(f'the {self.name} takes in sunlight, water, and CO^2, and it releases oxygen.')

    def protect_dna(self):
        print(f'the DNA replication of the {self.name}is protected by a cell wall as well as a nuclear membrane.')    

    def directional_movement(self):
        print(f'the {self.name} performs directional movements, such as phototropism.')  