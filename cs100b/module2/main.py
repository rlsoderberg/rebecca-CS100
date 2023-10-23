#import teacher and student classes
from teacher import Teacher
from student import Student

def main():
    #create people list
    people = [Teacher('quinn'), Student('anderson')]

    #person behaviors that are inherited by teacher and student
    for p in people:
        p.eat()
        p.sleep()
        #polymorphism = introduction specific to child class
        p.introduction()

    #remember to ask for 'type is'
    if type(p) is Teacher:
        p.answer_question()
    elif type(p) is Student:
        p.ask_question()

main()

