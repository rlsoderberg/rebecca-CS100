#set bill value
bill = 47.56

#print instructions
print("Your bill is $", bill, ".")
print("Input tip percentage of 10, 15, 20, or 25, to see tip amount and total price.")

#request input until a tip percentage of 10, 15, 20, or 25 is chosen
tippercentage=int(input("Enter a tip percentage of 10, 15, 20, or 25: "))
while tippercentage!=10 and tippercentage!=15 and tippercentage!=20 and tippercentage!=25:
    tippercentage=int(input("Invalid input. Please enter a tip percentage of 10, 15, 20, or 25: "))

#calculate tip and total        
tip = bill * (0.01 * tippercentage)
total = bill + tip

#print results
print(tippercentage,"% tip on bill of $",format(bill, '.2f'),"is $",format(tip, '.2f')," and total is $",format(total,'.2f'))
