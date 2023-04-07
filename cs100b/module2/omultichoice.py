from quizquestion import QuizQuestion

class Multichoice(QuizQuestion):
    def __init__(self, questionText, correctAnswer, choices):
        QuizQuestion.__init__(self, questionText, correctAnswer)
        self._choices = choices
        
    def showQuestion(self, questionNumber=0):
        QuizQuestion.showQuestion(self, questionNumber)
        
        for i in range(0, len(self._choices)):
            print('\t' + str(i+1) + ". " + self._choices[i])