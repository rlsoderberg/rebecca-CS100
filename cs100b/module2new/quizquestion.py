class QuizQuestion:
    def __init__(self, questionText, correctAnswer):
        self._questionText = questionText
        self._correctAnswer = correctAnswer
        
    def showQuestion(self, questionNumber=0):
        if questionNumber != 0:
            print('Question ' + str(questionNumber) + '. ', end='')
        print(self._questionText)
        
    def checkAnswer(self, response):
        if self._correctAnswer == response:
            return True
        else:
            return False

    