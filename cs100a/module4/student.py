#ok!!! i'm not as lost as i thought i was, but let me just put this in here...
class Student():
    #oh great, so that was where i saw the constructor with the parentheses!!!
    #it was later in the lesson!!!
    def __init__(self, name = '', ID = -1, birthdate = '1/1/2000'):
        """
        Create a default statement
        a default statement???
        does that mean uhhh, these things?
        i guess it kind of makes sense to do it this way
        since the thing where you initialize a class all at once by giving the variables in the parentheses...
        well, it doesn't really make much sense
        it's kinda fun tho!!!
        """
        #so i guess what i don't entirely understand is how these things are working down here
        #like, if i take them out...
        #well, if i take them out, it still works
        #but i get that initialization is cool and stuff!!!
        #THAT'S AN ASK, I SUPPOSE
        self.name = name
        self.ID = ID
        self.birthdate = birthdate

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
        #sooo a parameter is in parentheses for behaviors, but an argument is in parentheses for function?
        #oh nvm its both
        #uhh, it looks like the parameter is the place for the thing, and the argument is the actual thing?
        #that makes sense
        #i could just be, like, documenting classes all over the place right now!
        print(f'{self.name} is doing homework for {course} course.')

    def ask_question(self):
        """
        This student has a question for the instructor
        """
        print('Wait, what?')

stud = Student()

stud.name = 'Mary'
stud.ID = 10101
stud.birthdate = '1/1/1999'

print(stud.name)
stud.ask_question()

    