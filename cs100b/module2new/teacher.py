#1.1

from person import Person

class Teacher(Person):
    def __init__(self, name, ID=1,birthdate='1/1/1970',roomnumber=0):
        Person.__init__(self, name, ID, birthdate, roomnumber)

    def books(self, booknum):
        print(self.name+' stacks '+booknum+' books in reverse alphabetical order.')


