from person import Person

class Teacher(Person):
    def write_syllabus(self, course, school):
        print(self.name," wrote the syllablus for the ",course.name," course at ",school.name)
    def water_plants(self, indoor_plant, favorite_beverage, school):
        print(self.name," waters the ",indoor_plant," with ",favorite_beverage,", and is impugned by the ",school.location," ecological department.")
    def clean_board(self, favorite_beverage):
        print(self.name," obsessively draws pinstripes on the white board, then cleans it with ",favorite_beverage)