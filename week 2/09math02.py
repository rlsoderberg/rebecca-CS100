import random

#introduce program
print("Welcome to the math volcano.")
input("Leave explosives at the door. Identification please: ")

#create arrays for correct answers and user answers
problem_numbers = [0,1,2,3,4,5,6,7,8,9]
equations = ["5d + 3 = 13","14 - 3d = 2","9 - 2d = 3","8d + 2 = 50","2d + 16 = 40","12 - 2d = 2","7 = 49 - 6d","30 + 7d = 86","4d - 20 = 16","32 - 3d = -1"]
key = ["2", "4", "3", "6", "12", "5", "7", "8", "9", "11"]
correct = []
correct_count = 0

while correct_count <= 10:
    randgen = random.randint(0, 9)
    probnum = -1
    while probnum == -1:
        probnum = problem_numbers[randgen]
    print("Equation ",probnum,":")
    print(equations[probnum])
    valid = False
    while valid == False:
        try:
            inp = input("d = ")
            correct.insert(probnum, inp) # ?????????????????
            valid = True
            print("probnum: ",probnum) # + in print???
            print("correct = ",correct)
            print("key: ",key)
            print("correct[probnum]: ",correct[probnum])
            print("key[probnum]: ",key[probnum])
        except ValueError:
            print("Invalid input.")
"""
    if correct[probnum] == key[probnum]:
        print("Correct!")
        correct_count+=1
        problem_numbers[randgen] = -1
        probnum = -1
    else:
        print("Incorrect! Try another one!")
        
    
"""