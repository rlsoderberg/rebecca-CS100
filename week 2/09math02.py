import random

#introduce program
print("Welcome to the math volcano.")
input("Leave explosives at the door. Identification please: ")

#create arrays for correct answers and user answers
equations = ["5x + 3 = 13","14 - 3z = 2","9 - 2y = 3","8b + 2 = 50","2a + 16 = 40","12 - 2n = 2","7 = 49 - 6m","30 + 7c = 86","4s - 20 = 16","32 - 3d = -1"]
correct_ans = ["2", "4", "3", "6", "12", "5", "7", "8", "9", "11"]
ans = []
correct = 0

#get answer input from user
def answerget(x):
    print("Equation ",x,":")
    print(equations[x])
    valid = False
    while valid == False:
        try:
            inp = input()
            ans.insert(x, inp)
            valid = True
        except ValueError:
            print("Invalid input.")

def answermatch(x):
    if ans[x] == correct_ans[x]:#?????????????
        print("Correct!")
        return True
    else:
        print("Incorrect! Try again!")
        return False

while correct <= 10:
    rand = random.randint(0, 9)
    answerget(rand)
    if answermatch(rand) == True:#?????????????
        print("CORRECT!")
        correct+=1
