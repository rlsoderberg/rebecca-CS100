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

    mc = Multichoice('where is Whitworth?', '3', ['Seattle', 'Walla Walla', 'Spokane', 'London'])
    tf = TrueFalse('ransomware attacks are bad', '1')
    fill = FillInTheBlank('Coding is _______________', 'fun', 5)
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
















#multiple choice student: favorite animal (beetle, octopus, capybara, barracuda)




#yesno: will you color a picture of this animal?




#fillin: what writing implement will you use to color the animal




#story: how was your implement / animal composition received at the coloring competition?










#multiple choice teacher: favorite beverage (eggnog, whiskey, coca cola, ginger ale)




#yesno: are you going to water your blants with beverage?




#fillin: what kind of plant will you water with beverage?




#story: how did your plant like being watered with beverage?










#multiple choice driver: favorite food (banana, ravioli, broccoli, enchilada)




#yesno: do you want a map to find food?




#fillin: what type of roadwork lies between you and chimichangas?




#story: how did your map help you navigate roadwork, to chimichangas?

