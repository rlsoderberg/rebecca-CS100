weeknum = ["Monday",'Tuesday','Wednesday','Thursday','Friday',"Saturday","Sunday"]
expressions = ["0"," some moon-themed mittens.\n"
                " a football helmet for the Super Bowl.\n",
                " student costumes for the Hump Day Bonanza.\n",
                " a version of their favorite Brian Eno album cover, such as Thursday's Child.\n",
                " a full-body suit to keep them safe over the weekend.\n",
                " an avant-garde piece, while at a party.\n"
                " a cozy habit for their favorite monastic orders.\n"
]
#course class & functions
class Course:
    name = ''
    classroomnumber = -1
    credits = 0  
    
    def makeassignment(self, weekday, xp):
        print("It is ",weekday, ", so ",self.name + ' is giving an assignment for students to knit',xp)

    def kickout(self, subject, weekday, weekdayminusone):
        print("It is ",weekday,".")
        if weekday == "Friday":
            print(self.name, " is kicking out students today!\n")
        elif weekday == "Saturday" or weekday == "Sunday":
            print(self.name, "just kicked out some students, and is glad to have a weekend free.\n")
        else:
            daysleft = 5-wk 
            print(self.name, "has ",daysleft," days left until they can kick out some students.")

    def plandegree(self, weekday):
        print("Hello fellow staff people, it is ",weekday, "; what are we thinking about prerequisites?\n")

#generate weekday and calculate corresponding values before putting them into the function
import random
from datetime import datetime
dt = datetime.now()
wk = dt.isoweekday()
weekday = weeknum[wk-1]
weekdayminusone = weeknum[wk-2]
xp = expressions[wk-1]

#print results
course01 = Course()
course01.name = 'Knitting'
course01.classroomnumber = 307
course01.credits = 3
print("\n")
course01.makeassignment(weekday, xp)
course01.kickout('Computer Science', weekday, weekdayminusone)
course01.plandegree(weekday)