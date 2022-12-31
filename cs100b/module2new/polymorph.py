#2.1


from teacher import Teacher
from student import Student

def main():
    people = [Teacher('smith'), Student('jones')]

    for p in people:
        p.introduction()
        p.sleep()
        p.eat()

        if type(p) is Teacher:
            p.lecture('quantum biology')
        elif type(p) is Student:
            p.study()

if __name__ == '__main__':
    main()