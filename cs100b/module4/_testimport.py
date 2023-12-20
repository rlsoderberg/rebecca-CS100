class firstclass:
    def __init__(self, problem = ''):
        self.problem = problem

    #remember to give argument of self!!!
    def print_problem(self):
        print(f'my problem is {self.problem}.')