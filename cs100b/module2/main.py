from student import Student
from teacher import Teacher
from driver import Driver

def main():
    t = Teacher("Halbog")
    s = Student("Webfin")
    d = Driver("Pungap")

    t.school.name = "Lakewood"
    s.school = "Sunnydale"
    s.writing_implement = "pen"
    s.favorite_animal = "capybaras"
    d.favorite_food = "chimichangas"

    t.write_syllabus("chemistry", t.school)
    s.coloring_book(s.writing_implement,s.favorite_animal,s.school)
    d.foodmap(d.favorite_food)

if __name__ == "main":
    main()
