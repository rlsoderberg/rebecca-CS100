#4.3

class QuizQuestion:
    def __init__(self, questionText, correctAnswer, gradelevel=0):
        self._questionText = questionText
        self._correctAnswer = correctAnswer
        self.gradelevel = gradelevel
        
    def showQuestion(self, questionNumber=0):
        if questionNumber != 0:
            print('Question ' + str(questionNumber) + '. ', end='')
        print(self._questionText)
        
    def checkAnswer(self, response):
        if self._correctAnswer == response:
            return True
        else:
            return False

    