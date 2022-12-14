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

def main():
    t = Teacher('smith')
    s = Student('jones')

    s.sleep()
    t.eat()
    smc = Multichoice("what is your favorite animal?", '3', ['beetle', 'octopus', 'capybara', 'barracuda'])
    tmc = Multichoice("what is your favorite beverage?", '3', ['eggnog', 'whiskey', 'coca cola', 'ginger ale'])
    dmc = Multichoice('what is your favorite food', '4', ['banana', 'ravioli','broccoli','enchilada'])
    stf = TrueFalse('you will color a picture of this animal', '1')
    ttf = TrueFalse('you will water your plants with this beverage', '2')
    dtf = TrueFalse('you want a map to find this food', '1')
    sfill = FillInTheBlank('You color in the ANIMAL using a _______________ writing implement', 'sharpie', 5)
    tfill = FillInTheBlank('Instead, you water your _______________ with the BEVERAGE', 'desk', 5)
    dfill = FillInTheBlank('There is _______________ roadwork between you and the chimichangas', 'asphalt melting', 5)
    exam = [[smc, stf, sfill],[tmc, ttf, tfill],[dmc, dtf, dfill]]

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
    for i in range(0, len(exam[b])):
        exam[b][i].showQuestion(i+1)
        print('> ', end="")
        resp = maine(type, blanky)
        if exam[b][i].checkAnswer(resp) == True:
            print('well done')
        else:
            print('incorrect, sorry')




if __name__ == '__main__':
   main()