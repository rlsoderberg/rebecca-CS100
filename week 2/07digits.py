#input functions
def inputio():
    valid = False
    while valid == False:
        try:
            score = input("Enter score: ")
            valid = True
        except ValueError:
            print("Invalid Input!")
    return score

def input2():
    x = inputio()
    while x == "":
        print("I didn't hear you!")
        x = inputio()
    return x

score = input2()
letters = []
#make use of nice python array selector thing 'letter' to make an array of letters
for letter in score:
    letters.append(letter)

digits = []

#put digits in digits array
for s in letters:
    if s.isdigit():
        digits.append(s)

#concatenate string from digits
d = ""
for s in range (0, len(digits)):
    d = (d + digits[s])

print("Digits from score: ",d)