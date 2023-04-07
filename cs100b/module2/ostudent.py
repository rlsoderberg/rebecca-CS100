#1.4
#3.1

from person import Person

class Student(Person):
    def __init__(self, name, ID=0,birthdate='1/1/2000',gradelevel=0,classname=''):
        Person.__init__(self, name, ID, birthdate, gradelevel, classname)

    def study(self):
        print(self.name+'is studying.')
    
    def procrastinating(self,course):
        print(self.name+'is procrastinating on their'+course+'course.')
    
    def ask_question(self):
        print('Wait, what?')

    def introduction(self):
        sp = self.name.split("")
        print('I go by the name of '+sp.upper())