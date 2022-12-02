from person import Person

class Student(Person):
    def do_homework(self, course, school):
        print(self.name," did homework for the ",course.name," course at ",school.name)
    def coloring_book(self, writing_implement, favorite_animal, school):
        print(self.name, "colors a picture of the ",favorite_animal,", using a ",writing_implement,". ",self.name,"submits it to the ",school.location," coloring contest")
    def existential_crisis(self,favorite_animal):
        print(self.name," gazes into the mirror, wondering, who is ",self.name,"?",self.name," feels the ",favorite_animal," raging inside.")
