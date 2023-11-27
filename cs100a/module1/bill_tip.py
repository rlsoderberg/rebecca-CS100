#set variable for bill
bill = 47.56
#display bill to user
print(f'your bill is ${bill}.')

#request for user to choose a tip amount
print("Please select a tip amount:")

#initialize tiplist and input variable
tiplist = [0, 10, 15, 20, 25]
i = 0

#limit input to given options
while i != '1' and i != '2' and i != '3' and i != '4':
    i = input(f'1. {tiplist[1]}% 2. {tiplist[2]}% 3. {tiplist[3]}% 4. {tiplist[4]}%  ')

#select tiplevel corresponding to input
tiplevel = tiplist[int(i)]

#calculate tip and total bill, based on tiplevel
tip = 0.01 * tiplevel * bill
total = bill + tip
print(f'your tip is ${tip}')
print(f'your total is ${total}')

