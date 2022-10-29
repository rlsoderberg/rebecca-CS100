import random


#input functions
def inputio():
    valid = False
    while valid == False:
        try:
            x = input()
            while x == "":
                print("Out of range!")
                x = int(input())
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

#introduce program
print("Welcome to the math volcano.")
print("Leave explosives at the door. Identification please: ")
name = inputio()


#create arrays for correct answers and user answers
problem_numbers = [0,1,2,3,4,5,6,7,8,9]
equations = ["5d + 3 = 13","14 - 3d = 2","9 - 2d = 3","8d + 2 = 50","2d + 16 = 40","12 - 2d = 2","7 = 49 - 6d","30 + 7d = 86","4d - 20 = 16","32 - 3d = -1"]
key = ["2", "4", "3", "6", "12", "5", "7", "8", "9", "11"]
user = []
correct_count = 0
genmax = 9
turncount = 0

while correct_count < 10:
    randgen = random.randint(0, genmax)
    probnum = -1
    while probnum == -1:
        probnum = problem_numbers[randgen]
    print("Equation ",probnum,":")
    print(equations[probnum])
    print("d = ")
    inp = inputio()
    keyloc = key.index(inp)
    if probnum != keyloc: 
        print("Incorrect!")
    elif probnum == keyloc:
        print("Correct!")
        correct_count += 1
        key.remove(key[keyloc])
        equations.remove(equations[probnum])

    print("Subject ",name,": You have solved ",correct_count," equations correctly.")
    genmax -= 1
    turncount += 1

percent = (10/turncount)*100
tempgen = random.randint(100, 1000)
conversion = (percent / 100) * tempgen
print("Subject ",name,": You achieved ",percent,"% accuracy, at a temperature of ",tempgen," degrees.")
print("You have achieved a temperature conversion score of ",conversion)
