string = input("Enter score: ")

array = []

for letter in string:
    array.append(letter)

digits = []

for s in array:
    if s.isdigit():
        digits.append(s)

d = ""
for s in range (0, len(digits)):
    d = (d + digits[s])

print(d)