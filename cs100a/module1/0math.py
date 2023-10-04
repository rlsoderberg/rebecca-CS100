import random

#input function
#valid integers only

def int_input_function():
    valid = False
    while valid == False:
        try:
            x = int(input())
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
    rando = random.randint(0,9)
    while rando in prob_seq:
        rando = random.randint(0,9)
    prob_seq.append(rando)
    print(f"\n{x + 1} :  {equation_strings[rando]}")
    user_ans = 0
    print("Input answer: ")
    user_ans = int_input_function()
    if int(user_ans) == answers[rando]:
        print("correct")
        correct += 1
    elif int(user_ans) != answers[rando]:
        print("incorrect\n")
        print(f"{equation_strings[rando]}")
        print(f"x = {answers[rando]}\n")


name = ""
ready = ""
name = input("what is your name? ")
print(f"welcome, {name}, to the Tutorializer.\n")
print("Are you ready to be Tutorialized? Y/N")
ready = ready_input_function()
if ready == "Y":
    print("Let's go!")
elif ready == "N":
    print("Too bad! You cannot escape the Tutorializer!")


#we are importing random so that we can randomize the problem sequence
#oh right, i just looked, and this is the one where i got way overly elaborate with the math volcano
#i'm going to try to get through pretty fast, so that i can conserve my precious bodily fluids

#array of equation strings
equation_strings = ["5x + 3 = 13", "14 - 3x = 2", "9 - 2x = 3", "8x + 2 = 50", "2x + 16 = 40", 
                    "12 - 2x = 2", "7 = 49 - 6x", "30 + 7x = 86", "4x + 20 = 56", "3x - 3 = 39"]
#array of answer ints
answers = [2, 4, 3, 6, 12, 5, 7, 8, 9, 14]

#random number
rando = 0
#array of random numbers
prob_seq = []
correct = 0

for x in range (0, 10):
    math_problem(prob_seq, equation_strings)
    
      

