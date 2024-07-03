class Student():
    def __init__(self, name = '', ID = -1, birthdate = '1/1/2000'):
        """
        Create a default statement
        """
        self.name = name
        self.ID = ID
        self.birthdate = birthdate

    #make sure to indent all of your functions correctly
    def study(self):
        """
        Time to study
        """
        print(f'{self.name} is studying')

    def do_homework(self, course):
        """
        Time to do homework

        Parameters:
            course(str): The course to do homework for
        """
        #parameter is the place for the thing, and the argument is the actual thing you pass in
        print(f'{self.name} is doing homework for {course} course.')

    def ask_question(self):
        """
        This student has a question for the instructor
        """
        print('Wait, what?')

#create student object
stud = Student()

#set variables for student object
stud.name = 'Mary'
stud.ID = 10101
stud.birthdate = '1/1/1999'

#print variable, execute behavior
print(stud.name)
stud.ask_question()

    