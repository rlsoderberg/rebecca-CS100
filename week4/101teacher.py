weeknum = ["Monday",'Tuesday','Wednesday','Thursday','Friday',"Saturday","Sunday"]
expressions = ["0"," some late papers that were due on Friday.\n"
                " presentations for the Tuesday/Thursday class.\n",
                " student costumes for the Hump Day Bonanza.\n",
                " final projects for the Pre-Friday Night Class.\n",
                " final projects for the Actual Friday Night Class.\n",
                " their own cooking skills, which could use some practice.\n"
                " the existential dread that wells up within them every weekend.\n"
]
#teacher class & functions
class Teacher:
    name = ''
    officenumber = -1
    birthdate = '1/1/2000'   
    
    def grade(self, weekday, xp):
        print("It is ",weekday, ", so ",self.name + ' is trying to grade',xp)

    def lecture(self, subject, weekday):
        print("It is ",weekday, ", so ",self.name + ' is giving a lecture on ',subject,".\n")

    def ask_question(self, weekday, weekdayminusone):
        print("Hello student, it is ",weekday, "; did you do your homework from ",weekdayminusone,"?\n")

#generate weekday and calculate corresponding values before putting them into the function
import random
from datetime import datetime
dt = datetime.now()
wk = dt.isoweekday()
weekday = weeknum[wk-1]
weekdayminusone = weeknum[wk-2]
xp = expressions[wk-1]

#print results
teacher01 = Teacher()
teacher01.name = 'Mrs. Pringles'
teacher01.ID = 106
teacher01.birthdate = '1/1/1975'
print("\n")
teacher01.grade(weekday, xp)
teacher01.lecture('Computer Science', weekday)
teacher01.ask_question(weekday, weekdayminusone)