#request user input
score = input("Enter score: ")

letters = []
#make use of nice python array selector thing 'letter', append 
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

print(d)