#i don't know!!! i stashed this and main in a doc when i went and deleted some commits, hahaha oh dear
#lesson learned: do not store code in google docs

class QuizQuestion:

    def __init__(self, questionText, correctAnswer):
       self._questionText = questionText
       self._correctAnswer = correctAnswer

    def showQuestion(self, questionNumber = 0):
       if questionNumber !=0:
           #i don't really get the point of this end parameter!!!
           print('Question ',str(questionNumber),'. ',end='')

       print(self.questionText)



   #you should probably put most of this outside

    def getAnswer(self,response):
       #getanswer
       while len(self._correctAnswer) != len(response):
           if len(self.correctAnswer) < len(response):
               print('We are looking for something a little longer!')
           elif len(self.correctAnswer) > len(response):
               print('We are looking for something a little shorter!')
           #getanswer
       print('You got it!')


