#remember, you don't initialize the variables up here
class Course():
    #is it more efficient to give initial values down below? this way kind of makes sense to me? maybe?
    def __init__(self, ID = 0, class_name='', room=0, time = '', teacher = ''):
        self.class_name = class_name
        self.ID = ID
        self.room = room
        self.time = time
        self.teacher = teacher

    def location(self):
        print(f'{self.class_name} is taught in room {self.room} at {self.time}.')

    def teacher(self):
        print(f'the {self.time} session of {self.class_name} is taught by {self.teacher}')

    def due(self, project):
        print(f'the {project} project is due today in {self.class_name}.')

#can we set variables like this?
math101D = Course(134, "Math 101D", 240, 'T/TH 1 PM', "Hendrix")
print(f'course ID: {math101D.ID}')
math101D.due('Graphing Wing Size')

    


    