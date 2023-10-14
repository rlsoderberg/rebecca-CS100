class Eukaryote:
    #for some bizarre reason it only worked when i copy and pasted from lesson!!! whyyyy
    def __init__(self, name = '', species='', kingdom='', cellularity='', feeding='', reproduction=''):
    #and now it's not accepting my multiline comment!!! why is my program being so tweaky???
    #is it because i just deleted a whole bunch of files? because i did... and i messed with module 2 
    #because it was being weird and putting pycache on the same line as the folder title so i just
    #uh, kind of tried to delete the whole folder? not sure what happened after that?
    #anyway, here is my multiline comment about what i originally programmed
    #which i will now have to put in single line comments!!! grrr

    #no, literally, this is what i had before
    #isn't the only difference the spaces??????????
    #def __init__(self, species = '' kingdom = '', cell_count = '', feeding = '', reproduction = ''):
 
        self.name = name
        self.species = species
        self.kingdom = kingdom
        self.cellularity = cellularity
        self.feeding = feeding
        self.reproduction = reproduction
    
    def protect_dna(self):
        print(f'you try to disrupt the DNA replication of the {self.name}, but a nuclear membrane gets in the way.')

class Plant(Eukaryote):
    def __init__(self, name = '', species='', kingdom='', cellularity='', feeding='', reproduction=''):
        self.name = name
        self.species = species
        self.kingdom = kingdom
        self.cellularity = cellularity
        self.feeding = feeding
        self.reproduction = reproduction
    
    def photosynthesis(self):
        (f'you give the {self.name} some sunlight, water, and CO^2 and it gives you some oxygen.')

    def phototropism(self, lightsource):
        (f'you shine a {lightsource} on the {self.name}, and it turns toward the {lightsource}.')

class Fungus(Eukaryote):
    def __init__(self, name = '', species='', kingdom='', cellularity='', feeding='', reproduction=''):
        self.name = name
        self.species = species
        self.kingdom = kingdom
        self.cellularity = cellularity
        self.feeding = feeding
        self.reproduction = reproduction
    
    #next i get to research fungal behavior...
    #now, technically these behaviors will not be UNIVERSAL to all fungi... 
    #do class behaviors have to be universal???




    





    def protect_dna(self):
        print("DNA IS PROTECT")