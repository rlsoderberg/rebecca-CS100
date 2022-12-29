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
    
    sp = StoryProblem('What is the internet?','A series of tubes',['A big truck','Something you dump something on'],5,'arch., early 2000s', 'Ask Ted')
    mc = Multichoice("What is your favorite animal?", '3', ['Beetle', 'Octopus', 'Capybara', 'Barracuda'])
    tf = TrueFalse('There is a completely unrelated tree outside my window.', '1')
    fill = FillInTheBlank('Time is _______________ .', 'mushroom', 5)

    exam = [sp, mc, tf, fill]
    
    for i in range(0, len(exam)):
        exam[i].showQuestion(i+1)
        resp = input('> ')
        if exam[i].checkAnswer(resp) == True:
            print('well done')
        else:
            print('incorrect, sorry')

if __name__ == '__main__':
    main()