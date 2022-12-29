from teacher import Teacher
from student import Student

from storyproblem import StoryProblem
from multichoice import Multichoice
from fillin import FillInTheBlank
from truefalse import TrueFalse

def main():
    t = Teacher('smith')
    s = Student('jones')

    s.sleep()
    t.eat()
    
    mc = Multichoice("What is your favorite animal?", '3', ['beetle', 'octopus', 'capybara', 'barracuda'])
    tf = TrueFalse('There is a completely unrelated tree outside my window.', '1')
    fill = FillInTheBlank('Time is _______________ .', 'mushroom', 5)

    exam = [mc, tf, fill]
    
    for i in range(0, len(exam)):
        exam[i].showQuestion(i+1)
        resp = input('> ')
        if exam[i].checkAnswer(resp) == True:
            print('well done')
        else:
            print('incorrect, sorry')

if __name__ == '__main__':
    main()