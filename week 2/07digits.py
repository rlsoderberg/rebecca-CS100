#input function
def inputio():
    valid = False
    while valid == False:
        try:
            x =  input()
            while x == "":
                print("Out of range!")
                x = input()
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

print("Enter score: ")
score = inputio()
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

print("Digits within score: ",d)