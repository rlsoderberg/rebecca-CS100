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

    mc = Multichoice('where is Whitworth?', '3', ['Seattle', 'Walla Walla', 'Spokane', 'London'])
    tf = TrueFalse('ransomware attacks are bad', '1')
    fill = FillInTheBlank('Coding is _______________', 'fun', 5)
    exam = [mc, tf, fill]

    for i in range(0, len(exam)):
        exam[i].showQuestion(i+1)
        print('> ', end="")
        resp = maine(type, blanky)
        if exam[i].checkAnswer(resp) == True:
            print('well done')
        else:
            print('incorrect, sorry')




if __name__ == '__main__':
   main()