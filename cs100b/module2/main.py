from student import Student
from teacher import Teacher
from driver import Driver

def main():
    t = Teacher("Halbog")
    s = Student("Webfin")
    d = Driver("Pungap")

    t.hello()
    t.write_syllabus("chemistry", "Lakewood")
    s.coloring_book("pen","capybaras","Sunnydale")
    d.foodmap("chimichangas")

if __name__ == "__main__":
    main()
