#grocery list reevaluation is the completion of all things
f = open("grocery_list.txt", 'r')
#initialize lineno
lineno = 1
#loop through lines in text opened through file variable
for line in f:
    #strip lineno
    if lineno < 4:
        print(str(lineno)+": "+line.strip())
    elif lineno >= 4:
        print(line.strip())
    #question user about purchase decision
    if lineno < 4:
        print("would you REALLY like to make this purchase?")
        #accept input
        yes = input()
    #advance lineno
    lineno = lineno + 1

f.close()



