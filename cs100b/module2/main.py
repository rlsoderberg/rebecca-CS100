from teacher import Teacher
from student import Student
from busdriver import Busdriver

def main():

    #list of people (all inheriting from person class)
    people = [Student('smith'), Teacher('jones'), Busdriver('williams')]

    #for loop to run shared behaviors & run specific behaviors, based on child class
    for p in people:
        p.introduction()
        p.eat()
        p.sleep()

        if type(p) is Teacher:
            p.teach()
        elif type(p) is Student:
            p.ask_question()
        elif type(p) is Busdriver:
            p.pull_over()
        print('\n')


#oh, i forgot to put the underscores around main! you have to do the weird underscores, even if it's quoted!
if __name__ == '__main__':
    main()
