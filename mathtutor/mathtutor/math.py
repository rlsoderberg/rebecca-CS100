from quizquestion import Quiz_Question()

#int input function, preventing blank & non-int input
def int_input_function():
    valid = False
    while valid == False:
        try: 
            result = int(input())
            if result == '':
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print('Invalid Input')
    return result

#main function displays questions & results
def main():
    #ask user for name
    name = input('what is your name? ')

    #initialize count of correct answers
    total_correct = 0

    #create quizquestion onject
    quizquestion = Quiz_Question()

    #generate problems_list
    problems_list = []
    for x in range(1, 10):
        #get question_string & answer from generate question function
        question_string, answer = quizquestion.generate_question(x)

        #request user input with int input function
        user_ans = int_input_function()

        #check answer with check function
        correct = quizquestion.check(answer, user_ans)
        
        #increment total correct by correct
        total_correct += correct

        #store problem info in prob_tuple
        prob_tuple = (question_string, answer, user_ans, correct)
        problems_list.append(prob_tuple)

    #display results
    print(f'you solved {total_correct} out of 10 problems correctly')

    #give user preparation before hitting them with the list of results
    input('press any key to see your full results')
    for x in problems_list:
        (n, p, a, u, c) = x
        if c == 1:
            correct = 'correct'
        else:
            correct = 'incorrect'
        print(f"problem {n}: {p}. correct answer: {a}. user answer: {u}. {correct}")

main()





