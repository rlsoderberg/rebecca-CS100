from quizquestion import QuizQuestion 

class FillInTheBlank(QuizQuestion):
    def __init__(self, questionText, correctAnswer, whereBlank):
        QuizQuestion.__init__(self, questionText, correctAnswer)
        self._whereBlank = whereBlank