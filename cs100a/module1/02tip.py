import sys
sys.path.append('../..')

from i import input_function

#set bill value
bill = 47.56

#print instructions
print("Your bill is $", bill, ".")
print("Input tip percentage of 10, 15, 20, or 25, to see tip amount and total price.")

#request input until a tip percentage of 10, 15, 20, or 25 is chosen
tippercentage = 0
while tippercentage!=10 and tippercentage!=15 and tippercentage!=20 and tippercentage!=25:
    #yes this single variable is kind of unnecessary but i think it's kind of cute?
    type_name = "int"
    percentage_input = input_function("int")
    tippercentage=int(percentage_input)

#calculate tip and total        
tip = bill * (0.01 * tippercentage)
total = bill + tip

#print results
print(tippercentage,"% tip on bill of $",format(bill, '.2f'),"is $",format(tip, '.2f')," and total is $",format(total,'.2f'))
