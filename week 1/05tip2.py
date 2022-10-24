#request user input of bill
valid=False
while valid == False:
    try:
        bill = float(input("Enter bill amount: "))
        valid = True
    except ValueError:
        print("Invalid input.")

#create array of tip percentages to display
percent = [10, 15, 20, 25]

#create arrays of tips and totals for each tip percentage
for x in range (0, 4):
    tip = bill * (0.01 * percent[x])
    total = bill + tip
    print(percent[x],"% tip on bill of $",format(bill, '.2f'),"is $",format(tip, '.2f')," and total is $",format(total,'.2f'))

#request user input of custom tip percentage
valid = False
while valid == False:
    try:
        userpercent = float(input("Please input desired tip percentage: "))
        valid = True
    except ValueError:
        print("Invalid input.")

tip = bill * (0.01 * userpercent)
total = bill + tip
print(userpercent,"% tip on bill of $",format(bill, '.2f'),"is $",format(tip, '.2f')," and total is $",format(total,'.2f'))