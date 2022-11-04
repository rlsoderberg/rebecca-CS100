import random


#input functions
def inputio():
    valid = False
    while valid == False:
        try:
            x = input()
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
equations = [("5d + 3 = 13", "2", ""),("14 - 3d = 2","4",""),("9 - 2d = 3","3",""),("8d + 2 = 50","6",""),("2d + 16 = 40","12",""),("12 - 2d = 2","5",""),("7 = 49 - 6d","7",""),("30 + 7d = 86","8",""),("4d - 20 = 16","9",""),("32 - 3d = -1","11","")]
user = []
correct_count = 0
genmax = 9
turncount = 0

while correct_count < 10:
    randgen = random.randint(0, genmax)
    probnum = -1
    while probnum == -1:
        probnum = problem_numbers[randgen]

    print("\n")
    print(name, "Equation ",probnum,":")
    current = list(equations[probnum])
    print(current[0])
    print("d = ")
    current[2] = inputio()
    if current[1] == current[2]:
        print("Correct!")
        correct_count += 1
        equations.remove(equations[probnum])
    else:
        print("Incorrect!")

    print("Subject ",name," has solved ",correct_count," equations correctly.\n")
    print("Perform any action to commence.")
    inputioma = inputio()
    genmax -= 1
    turncount += 1

percent = (10/turncount)*100
tempgen = random.randint(100, 1000)
conversion = (percent / 100) * tempgen
print("Subject ",name," has achieved ",percent,"% accuracy, at a temperature of ",tempgen," degrees.")
print("You have achieved a temperature conversion score of ",conversion)
