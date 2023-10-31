import random

class Quiz_Question():
    def __init__(self, num = 0, question = '', answer = 0, user_ans = 0, grade_level = 0):
        self.num = num
        self.question = question
        self.answer = answer
        self.user_ans = user_ans
        self.grade_level = grade_level

    #always include self as the first argument otherwise compiler complains about positional arguments
    def generate_question(self, num):
        """
        generate random variables
        print question based on these variables, and create question string
        calculate correct answer

        parameters: 
            num(int): the number of the problem (1 - 10)
        """
        #random variables for questions
        rand1 = random.randrange(1, 10)
        rand2 = random.randrange(1, 10)

        #create question string with num and these random variables
        #remember to convert everything to a string
        question_string = str(num) + '. ' + str(rand1) + ' - ' + str(rand2) + ' = '

        #calculate correct answer
        answer = rand1 - rand2

        #print question
        print(f'{question_string}')

        return question_string, answer

    #paramaters for correct answer, and user answer, to see if they are the same
    def check(self, answer, user_ans):
        """
        generate random variables
        print question based on these variables, and create question string
        calculate correct answer

        parameters: 
            answer(int): the correct answer of the problem
            user_ans(int): the answer entered by the user
        
        """
        #see whether user answer = actual answer, generate correct variable
        if user_ans == answer:
            print('correct')
            correct = 1
        else:
            print('incorrect')
            correct = 0

        #generate correct string based on correct variable
        if correct == 1:
            correct_string = 'correct'
        else:
            correct_string = 'incorrect'

        #return correct variable and correct string
        return correct, correct_string

    