weeknum = ["Monday",'Tuesday','Wednesday','Thursday','Friday',"Saturday","Sunday"]
expressions = ["0"," the number of beats in the song Blue Monday by New Order.\nThe song is about 7:25, and its BPM is 130.\n",
                " the number of beats in Mars from Holst's The Planets.\nThe movement has 185 measures, with 5 beats per measure.\n"
                " the number of beats in the Addams Family theme song.\nThe song is 50 seconds long, with 120 BPM.\n",
                " the length of the mixtape Thursday by The Weeknd.\n Its songs are 5:49, 4:56, 5:20, 6:58, 3:34, 5:30, 8:06, 3:50, and 5:53.\n",
                " the number of beats in the song Friday I'm In Love by The Cure.\nThe song is about 3:25, and its BPM is 136.\n",
                " the number of beats in the song A Roller Skating Jam Named Saturdays by De La Soul.\nThe song is about 4:00, and with 114 BPM.\n",
                " the number of beats in the song Sunday Morning by Lou Reed.\nThe song is about 2:50, and its BPM is 108.\n"
]
#student class & functions
class Student:
    name = ''
    ID = -1
    birthdate = '1/1/2000'   
    
    def math(self, weekday, xp):
        print("It is ",weekday, ", so ",self.name + ' is trying to calculate',xp)

    def encyclopedia(self, subject, weekday):
        print("It is ",weekday, ", so ",self.name + ' is looking up ',subject,".\n")

    def ask_question(self, weekday):
        print("How did it get to be ",weekday, " already?\n")

#generate weekday and calculate corresponding values before putting them into the function
import random
from datetime import datetime
dt = datetime.now()
wk = dt.isoweekday()
weekday = weeknum[wk-1]
xp = expressions[wk-1]
#print results
stud01 = Student()
stud01.name = 'Mary'
stud01.ID = 10101
stud01.birthdate = '1/1/1999'
print("\n")
stud01.math(weekday, xp)
stud01.encyclopedia('Computer Science', weekday)
stud01.ask_question(weekday)