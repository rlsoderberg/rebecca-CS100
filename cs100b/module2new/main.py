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
    print("are you 1. a student, 2. a teacher, or 3. a driver?")
    typo = maine(type, blanky)
    if typo == '1':
        print("valid input.")
        return typo
    while typo != '1':
        if typo == '1':
            print("valid input.")
            return typo
        else:
            print("invalid input.")
            print("are you 1. a student, 2. a teacher, or 3. a driver?")
            typo = maine(type, blanky)

    return typo
        

def checkio(answ):
    if QuizQuestion.checkAnswer(answ) == True:
        print('well done')
    else:
        print('incorrect, sorry')

def student(num):
    propnum = num + 1
    if num == 0:
        QuizQuestion.showQuestion(propnum)
        mc = Multichoice("what is your favorite animal?", '3', ['beetle', 'octopus', 'capybara', 'barracuda'])
        checkio(mc)
    elif num == 1:
        QuizQuestion.showQuestion(propnum)
        tf = TrueFalse('you will color a picture of '+mc, '1')
        checkio(tf)
    elif num == 2:
        QuizQuestion.showQuestion(propnum)
        fib = FillInTheBlank('You color in the'+mc+' using a _______________ writing implement','sharpie',10)
        checkio(fib)

def main():
    nums = [0,1,2]
    selectoni = selecto()
    for b in nums:
        student(b)

    



if __name__ == '__main__':
   main()