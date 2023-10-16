from i import input_function, int_input_function

class Quiz_Question:
    def __init__(self, question = "", answer="", grade_lvl="", user_ans = ""):
        self.question = question
        self.answer = answer
        self.grade_lvl = grade_lvl
        self.user_ans = user_ans

    def get_question(self):
        print("Input a math problem:")
        self.question = input_function()

    def get_answer(self):
        print(f"Input the answer to {self.question}:")
        self.answer = input_function()

    def get_grade_lvl(self):
        print(f'Enter the grade level for the math problem {self.question}:')
        self.gradelvl = input_function()

    def get_user_ans(self):
        self.user_ans = 0
        print(f'\nProblem: {self.question}')
        print("Your Answer:")
        self.user_ans = int_input_function()

    def check_answer(self):
        this_correct = 0
        if int(self.user_ans) == int(self.answer):
            print("correct")
            this_correct = 1
        elif int(self.user_ans) != int(self.answer):
            print("\n\nincorrect\n")
            input("Press any key to see the correct answer.\n")
            print("\n\n\n\nCorrect Answer:")
            print(f"{self.question}")
            print(f"x = {self.answer}\n")
        return this_correct