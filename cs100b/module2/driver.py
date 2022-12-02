from person import Person

class Driver(Person):
    def drive(self, vehicle,school):
        print(self.name," is driving their ",vehicle.name," using a new map program made by students at ",school.name)
    def skywish(self, roadwork_type, favorite_food, school):
        print(self.name, " sees a ",roadwork_type," truck dropping ",favorite_food," around ",school.location)
    def foodmap(self,favorite_food):
        print(self.name," wonders, what if I had a map that led me to sources of",favorite_food,"?")