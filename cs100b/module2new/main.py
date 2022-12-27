from teacher import Teacher
from student import Student


from storyproblem import StoryProblem
from multichoice import Multichoice
from fillin import FillInTheBlank
from truefalse import TrueFalse


#input functions
import sys
sys.path.append("C:..\..")
from i import maine
#here's the stuff for i input
type = "str"
blanky = 1

answers = []
c = 0


def persona():
    t = Teacher('smith')
    s = Student('jones')

    s.sleep()
    t.eat()


def selecto():
    print("are you a student, a teacher, or a driver?")
    type = maine(type, blanky)
    while type != 'student' and type != 'teacher' and type!= 'driver':
        print("invalid input.")
        print("are you a student, a teacher, or a driver?")
        type = maine(type, blanky)
        if type == 'student':
            b = 0
        elif type == 'teacher':
            b = 1
        elif type == 'driver':
            b = 2

    return b
        

def checkio(exam, b):
    for i in range(0, len(exam[b])):
        #execute exam[b][i]
        exam[b][i].showQuestion(i+1)
        print('> ', end="")
        resp = maine(type, blanky)
        answers.append(exam[b][i])
        if exam[b][i].checkAnswer(resp) == True:
            print('well done')
        else:
            print('incorrect, sorry')
        c += 1

def main():
    b = selecto()

    #ideally i want to put these in, like, a list or something, so i can execute them up in checkio
    m0 = Multichoice("what is your favorite animal?", '3', ['beetle', 'octopus', 'capybara', 'barracuda'])
    m1 = Multichoice("what is your favorite beverage?", '3', ['eggnog', 'whiskey', 'coca cola', 'ginger ale'])
    m2 = Multichoice('what is your favorite food', '4', ['banana', 'ravioli','broccoli','enchilada'])
    t0 = TrueFalse('you will color a picture of '+m0, '1')
    t1 = TrueFalse('you will water your plants with '+m1, '2')
    t2 = TrueFalse('you want a map to find '+m2, '1')
    f0 = FillInTheBlank('You color in the'+m0+' using a _______________ writing implement','sharpie',536202)
    f1 = FillInTheBlank('Instead, you water your _______________ with the'+m1+'. ','desk',404728)
    f2 = FillInTheBlank('There is _______________ roadwork between you and your favorite'+m0+'restaurant.','asphalt melting',5479032)

    exam = [(m0, t0, f0),(m1,t1,f1),(m2,t2,f2)]

    #and then down here i can just be be like, checkio
    



if __name__ == '__main__':
   main()