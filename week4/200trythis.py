weeknum = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
expressions = ["0"," the number of beats in the song Blue Monday by New Order.\nThe song is about 7:25, and its BPM is 130.\n",
                " the number of beats in Mars from Holst's The Planets.\nThe movement has 185 measures, with 5 beats per measure.\n"
                " the number of beats in the Addams Family theme song.\nThe song is 50 seconds long, with 120 BPM.\n",
                " the length of the mixtape Thursday by The Weeknd.\n Its songs are 5:49, 4:56, 5:20, 6:58, 3:34, 5:30, 8:06, 3:50, and 5:53.\n",
                " the number of beats in the song Friday I'm In Love by The Cure.\nThe song is about 3:25, and its BPM is 136.\n",
                " the number of beats in the song A Roller Skating Jam Named Saturdays by De La Soul.\nThe song is about 4:00, and with 114 BPM.\n",
                " the number of beats in the song Sunday Morning by Lou Reed.\nThe song is about 2:50, and its BPM is 108.\n"
]

class Student:
    name = ''
    ID = -1
    birthdate = '1/1/2000' 

    def __init__(self, name='', ID=-1, birthdate='1/1/2000'):
        self.name = name
        self.birthdate = birthdate  
    
    def math(self, weekday, xp):
        print("It is ",weekday, ", so ",self.name + " is trying to calculate",xp)

    def encyclopedia(self, subject, weekday):
        print("It is ",weekday, ", so ",self.name + " is looking up ",subject,".\n")

    def ask_question(self, weekday):
        print("How did it get to be ",weekday, " already?\n")

stud01 = Student()
stud02 = Student('Susan', 11223, '6/1/2001')

print(vars(stud01))
print(vars(stud02))

dict = {}

names = open("names.txt").read().split("\n")
birthdates = open("birthdates.txt").read().split("\n")

"""
for x in range (200):
    dict[x] = Student()
    print("\nStudent ",x)
    dict[x].name = input("\nEnter student name: ")
    dict[x].birthdate = input("Enter student birthdate: ")
    print("\nStudent Id: ",x,"\nName: ",dict[x].name,"\nBirthdate: ",dict[x].birthdate)
"""
import random 

for x in range (200):
    random.shuffle(names)
    random.shuffle(birthdates)
    dict[x] = Student()
    dict[x].name = names[x]
    dict[x].birthdate = birthdates[x]
    print("\nStudent Id: ",x,"\nName: ",dict[x].name,"\nBirthdate: ",dict[x].birthdate)
