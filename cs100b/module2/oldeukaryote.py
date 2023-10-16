class Eukaryote:
    def __init__(self, name = '', species='', kingdom='', cellularity='', feeding='', reproduction=''):
 
        self.name = name
        self.species = species
        self.kingdom = kingdom
        self.cellularity = cellularity
        self.feeding = feeding
        self.reproduction = reproduction

    def protect_dna(self):
        print(f'the DNA replication of the {self.name}is protected by a nuclear membrane.')

    def directional_movement(self, external_stimulus):
        print(f'the {self.name} performs directional movements.')  

    def active_feeding(self, food):
        print(f'the {self.name} feeds actively on {food}.')
