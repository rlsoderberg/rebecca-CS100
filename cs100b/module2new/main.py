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

def examtype():
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


def main():
    t = Teacher('smith')
    s = Student('jones')

    s.sleep()
    t.eat()
    
    smc = Multichoice("what is your favorite animal?", '3', ['beetle', 'octopus', 'capybara', 'barracuda'])
    stf = TrueFalse('you will color a picture of '+smc, '1')
    sfib = FillInTheBlank('You color in the'+smc+' using a _______________ writing implement','sharpie',10)

    tmc = Multichoice("what is your favorite beverage?", '3', ['eggnog', 'whiskey', 'coca cola', 'ginger ale']) 
    ttf = TrueFalse('you will water your plants with '+tmc, '2')
    tfib = FillInTheBlank('you decide to water your _______________ with the'+tmc+'. ','desk',10)

    dmc = Multichoice('what is your favorite food', '4', ['banana', 'ravioli','broccoli','enchilada'])
    dtf = TrueFalse('you want a map to find '+dmc, '1')
    dfib = fib = FillInTheBlank('There is _______________ roadwork between you and the nearest'+dmc+'restaurant.','asphalt melting',10)

    exam = [(smc, stf, sfib),(tmc, ttf, tfib),(dmc, dtf, dfib)]
    
    for i in range(0, len(exam)):
        t = examtype()
        exam[i].showQuestion(i+1)
        resp = input('> ')
        if exam[i].checkAnswer(resp) == True:
            print('well done')
        else:
            print('incorrect, sorry')

if __name__ == '__main__':
    main()