#introduce program
print("Welcome to the math volcano.")
input("Leave explosives at the door. Identification please: ")

#create arrays for correct answers and user answers
correct_ans = [2, 4, 3, 6, 12, 5, 7, 8, 9, 14]
ans = []

#print equation
print("Equation 1:")
print("5x + 3 = 11") #x=2
#request user input, checking for int type
valid = False
while valid == False:
        try:
            ans.append(int(input("x = ")))
            valid = True
        except ValueError:
            print("Invalid input.")

print("Equation 2:")
print("14 - 3z = 2") #z=4
valid = False
while valid == False:
        try:
            ans.append(int(input("z = ")))
            valid = True
        except ValueError:
            print("Invalid input.")

print("Equation 3:")
print("9 - 2y = 3") #y=3
valid = False
while valid == False:
        try:
            ans.append(int(input("y = ")))
            valid = True
        except ValueError:
            print("Invalid input.")

print("Equation 4:")
print("8b + 2 = 50") #b=6
valid = False
while valid == False:
        try:
            ans.append(int(input("b = ")))
            valid = True
        except ValueError:
            print("Invalid input.")

print("Equation 5:")
print("2a + 16 = 40") #a=12
valid = False
while valid == False:
        try:
            ans.append(int(input("a = ")))
            valid = True
        except ValueError:
            print("Invalid input.")


print("Equation 6:")
print("12 - 2n = 2") #n=5
valid = False
while valid == False:
        try:
            ans.append(int(input("n = ")))
            valid = True
        except ValueError:
            print("Invalid input.")

print("Equation 7:")
print("7 = 49 - 6m") #m=7
valid = False
while valid == False:
        try:
            ans.append(int(input("m = ")))
            valid = True
        except ValueError:
            print("Invalid input.")

print("Equation 8:")
print("30 + 7c = 86") #c=8
valid = False
while valid == False:
        try:
            ans.append(int(input("c = ")))
            valid = True
        except ValueError:
            print("Invalid input.")

print("Equation 9:")
print("24s + 20 = 245") #s=9
valid = False
while valid == False:
        try:
            ans.append(int(input("s = ")))
            valid = True
        except ValueError:
            print("Invalid input.")

print("Equation 10:")
print("32d - 3 = 445") #d=14
valid = False
while valid == False:
        try:
            ans.append(int(input("d = ")))
            valid = True
        except ValueError:
            print("Invalid input.")

print(ans)
print("Hello")