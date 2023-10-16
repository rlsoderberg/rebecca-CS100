from eukaryote import Eukaryote

class Fungus(Eukaryote):
    def __init__(self, name = '', species='', kingdom='', cellularity='', feeding='', reproduction=''):
        self.name = name
        self.species = species
        self.kingdom = kingdom
        self.cellularity = cellularity
        self.feeding = feeding
        self.reproduction = reproduction

    def control_insect(self, insect):
        print(f"the {insect} comes into contact with {self.name}, and the {self.name} takes away the {insect}'s free will")

    def mycelium(self, connected_organism):
        print(f'the {self.name} connects to the {connected_organism} through a mycelial network, forming a symbiotic relationship.')

    def protect_dna(self):
        print(f'the DNA replication of the {self.name}is protected by a cell wall as well as a nuclear membrane.')

    def directional_movement(self):
        print(f'the {self.name} performs directional movements, such as spore dispersal.')  