#1.2

def WormholeVisitor(Person):

    def __init__(self, name, ID=2,birthdate='2/31/3200'):
        Person.__init__(self, name, ID, birthdate)

    def particularize(self, subject):
        print('I am investigating the subatomic particles of',subject)

    def timeline(self):
        print('I was born last Septober')