class Teacher:
    def __init__(self, name = '', office = 0, department = ''):
        """
        Create a default statement
        """
        self.name = name
        self.office = office
        self.department = department

    def ask_question(self, subject):
        """
        Parameters:
        subject(str): the subject that {self.name} is asking about
        """
        print(f'{self.name} asks a question about {subject}')
        
    def write(self, idea):
        """
        Parameters:
        idea(str): the idea that {self.name} is writing about
        """
        print(f'{self.name} writes about {idea}')
        
    def phone_call(self, recipient):
        """
        Parameters:
        recipient(str): the person that {self.name} is calling on the phone
        """
        print(f'{self.name} calls {recipient} on the phone.')

#create new teacher object, assign variables
teacher1 = Teacher()
teacher1.name = 'mr. bob'
teacher1.office = 309
teacher1.subject = 'horticulture'

#use variable, execute behavior
print(f"teacher name = {teacher1.name}")
teacher1.ask_question('ferns')
