from quizquestion import QuizQuestion

class StoryProblem(QuizQuestion):
    def __init__(self, questionText, correctAnswer, possibleIncorrectAnswers, totalPoints, parameters, walkthrough):
        QuizQuestion.__init__(self, questionText, correctAnswer)
        self._possibleIncorrect = possibleIncorrectAnswers
        self._totalPoints = totalPoints
        self._parameters = parameters
        self._walkthrough = walkthrough

