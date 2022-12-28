from teacher import Teacher
from student import Student


from storyproblem import StoryProblem
from multichoice import Multichoice
from fillin import FillInTheBlank
from truefalse import TrueFalse

from checkanswer import CheckAnswer


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
        

def checkio(answ):
    if CheckAnswer(answ) == True:
        print('well done')
    else:
        print('incorrect, sorry')

def student(num):
    if num == 0:
        mc = Multichoice("what is your favorite animal?", '3', ['beetle', 'octopus', 'capybara', 'barracuda'])
        checkio(mc)
    elif num == 1:
        tf = TrueFalse('you will color a picture of '+mc, '1')
        checkio(tf)
    elif num == 2:
        fib = FillInTheBlank('You color in the'+mc+' using a _______________ writing implement','sharpie',10)
        checkio(fib)

def teacher(num):
    if num == 0:
        mc = Multichoice("what is your favorite beverage?", '3', ['eggnog', 'whiskey', 'coca cola', 'ginger ale'])
        checkio(mc)
    elif num == 1:
        tf = TrueFalse('you will water your plants with '+mc, '2')
        checkio(tf)
    elif num == 2:
        fib = FillInTheBlank('you decide to water your _______________ with the'+mc+'. ','desk',10)
        checkio(fib)

def driver(num):
    if num == 0:
        mc = Multichoice('what is your favorite food', '4', ['banana', 'ravioli','broccoli','enchilada'])
        checkio(mc)
    elif num == 1:
        tf = TrueFalse('you want a map to find '+mc, '1')
        checkio(tf)
    elif num == 2:
        fib = FillInTheBlank('There is _______________ roadwork between you and the nearest'+mc+'restaurant.','asphalt melting',10)
        checkio(fib)

def main():
    nums = [0,1,2]
    type = selecto()
    if type == 0:
        for b in nums:
            student()
    if type == 1:
        for b in nums:
            teacher()
    if type == 2:
        for b in nums:
            driver()

    



if __name__ == '__main__':
   main()