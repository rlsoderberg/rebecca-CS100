import random

import sys
sys.path.append("..\..")
                
from i import input_function

#input function
#valid integers only

def int_input_function():
    valid = False
    while valid == False:
        try:
            x = int(input(f"x = "))
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

def ready_input_function():
    ready = ""
    while ready != "Y" and ready != "N":
        try:
            ready = input()
            if not ready:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return ready  

def math_problem(prob_seq, equation_strings):
    correct = 0
    rando = random.randint(0,9)

    while rando in prob_seq:
        rando = random.randint(0,9)
    prob_seq.append(rando)
    print(f"\n{x + 1} :  {equation_strings[rando]}")
    user_ans = 0
    print("Your Answer:")
    user_ans = int_input_function()
    correct_ans = answers[rando]
    if int(user_ans) == correct_ans:
        print("correct")
        correct = 1
    elif int(user_ans) != correct_ans:
        print("\n\nincorrect\n")
        input("Press any key to see the correct answer.\n")
        print("\n\n\n\nCorrect Answer:")
        print(f"{equation_strings[rando]}")
        print(f"x = {answers[rando]}\n")
    return [rando, correct, user_ans, correct_ans]

#random number, and array of random numbers, to randomize equation order
rando = 0
prob_seq = []
rand_list = []
user_ans_list = []
correct_list = []
correct_ans_list = []
#array of equation strings
equation_strings = ["5x + 3 = 13", "14 - 3x = 2", "9 - 2x = 3", "8x + 2 = 50", "2x + 16 = 40", 
                    "12 - 2x = 2", "7 = 49 - 6x", "30 + 7x = 86", "4x + 20 = 56", "3x - 3 = 39"]
correct = 0
#array of answer ints
answers = [2, 4, 3, 6, 12, 5, 7, 8, 9, 14]

name = ""
ready = ""
print("what is your name? ")
name = input_function()
print(f"welcome, {name}, to the Tutorializer.\n")
print("Are you ready to be Tutorialized? Y/N")
ready = ready_input_function()
if ready == "Y":
    print("Let's go!\n\n\n")
elif ready == "N":
    print("Too bad! You cannot escape the Tutorializer!")

#yeah, this is totally wack. it's not even working right now. can i just put this off until we do classes???
for x in range (0, 10):
    result = math_problem(prob_seq, equation_strings)
    rando = result[0]
    rand_list.append(rando)
    outside_correct = result[1]
    correct_list.append[outside_correct]
    user_ans = result[2]
    user_ans_list.append(user_ans)
    outside_correct_ans = result[3]
    correct_ans_list.append(outside_correct_ans)

    

print(f"\n\nCongratulations! You have answered {correct} math problems correctly!")
print(f"Your Tutorialization Level is {correct*10}%.\n")

input("Press any key to see a list of equations.\n")

#THIS DEFINITELY DOESN'T SEEM LIKE THE CORRECT WAY TO ARRANGE THE DATA
for x in rand_list:
    print(f"{equation_strings[rand_list[x]]}")
    print("Your Answer: ")
    print(f"x = {user_ans_list[x]}")
    if correct_list[x] == 1:
        print("Correct!")
    elif correct_list[x] == 0:
        print("Incorrect!\n\n")
        print(f"{equation_strings[rand_list[x]]}")
        print("Correct Answer: ")
        print(f"x = {correct_ans_list[x]}")
    x += 1



    
      

