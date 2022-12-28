from teacher import Teacher
from student import Student


from storyproblem import StoryProblem
from multichoice import Multichoice
from fillin import FillInTheBlank
from truefalse import TrueFalse

from quizquestion import QuizQuestion

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
        print("are you 1. a student, 2. a teacher, or 3. a driver?")
        typenum = maine(type, blanky)
        while typenum != 0:
            print("that is wrong")
            type = maine(type, blanky)

    return typenum
        

def checkio(answ):
    if QuizQuestion.checkAnswer(answ) == True:
        print('well done')
    else:
        print('incorrect, sorry')

def student(num):
    if num == 0:
        QuizQuestion.showQuestion(num + 1)
        mc = Multichoice("what is your favorite animal?", '3', ['beetle', 'octopus', 'capybara', 'barracuda'])
        checkio(mc)
    elif num == 1:
        QuizQuestion.showQuestion(num + 1)
        tf = TrueFalse('you will color a picture of '+mc, '1')
        checkio(tf)
    elif num == 2:
        QuizQuestion.showQuestion(num + 1)
        fib = FillInTheBlank('You color in the'+mc+' using a _______________ writing implement','sharpie',10)
        checkio(fib)

def main():
    nums = [0,1,2]
    type = selecto()
    if type == 0:
        for b in nums:
            student(b)

    



if __name__ == '__main__':
   main()