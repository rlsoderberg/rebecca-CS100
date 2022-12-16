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


def sfiller():
    print('You color in the', answers[c-2], ' using a _______________ writing implement')
    sfill = FillInTheBlank('', 'sharpie', 5)
    return sfill

def tfiller():
    print('Instead, you water your _______________ with the', answers[c-2], '. ')
    tfill = FillInTheBlank('', 'desk', 5)
    return tfill

def dfiller():
    print('There is _______________ roadwork between you and your favorite', answers[c-2], 'restaurant.')
    dfill = FillInTheBlank('', 'asphalt melting', 5)
    return dfill

def persona():
    t = Teacher('smith')
    s = Student('jones')

    s.sleep()
    t.eat()


def selecto():
    print("are you a student, a teacher, or a driver?")
    t = maine(type, blanky)
    while t != 'student' and t != 'teacher' and t!= 'driver':
        print("invalid input.")
        print("are you a student, a teacher, or a driver?")
        t = maine(type, blanky)
    if t == 'student':
        b = 0
    elif t == 'teacher':
        b = 1
    elif t == 'driver':
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
#i know this is bad, but i need to initialize these first somehow, right???
    smc = 0
    tmc = 0
    dmc = 0
    stf = 0
    ttf = 0
    dtf = 0
    sfill = 0
    tfill = 0
    dfill = 0

    exam = [[smc, stf, sfill],[tmc, ttf, tfill],[dmc, dtf, dfill]]

    #ideally i want to put these in, like, a list or something, so i can execute them up in checkio
    smc = Multichoice("what is your favorite animal?", '3', ['beetle', 'octopus', 'capybara', 'barracuda'])
    tmc = Multichoice("what is your favorite beverage?", '3', ['eggnog', 'whiskey', 'coca cola', 'ginger ale'])
    dmc = Multichoice('what is your favorite food', '4', ['banana', 'ravioli','broccoli','enchilada'])
    stf = TrueFalse('you will color a picture of this animal', '1')
    ttf = TrueFalse('you will water your plants with this beverage', '2')
    dtf = TrueFalse('you want a map to find this food', '1')
    sfill = sfiller()
    tfill = tfiller()
    dfill = dfiller()

    #and then down here i can just be be like, checkio
    



if __name__ == '__main__':
   main()