#2.2
from person import Person

class Chef(Person):
    def __init__(self, name='', birthdate='1/1/1985'):
        Person.__init__(self,name,birthdate)

    def makesoup(self, soup):
        print(self.name+'is making'+soup+'soup.')

    def clean(self):
        print(self.name+'is cleaning the entire kitchen')

    