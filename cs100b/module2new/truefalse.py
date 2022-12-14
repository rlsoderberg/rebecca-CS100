from multichoice import Multichoice

class TrueFalse(Multichoice):
    def __init__(self, questionText, correctAnswer):
        Multichoice.__init__(self, questionText, correctAnswer, ['true', 'false'])