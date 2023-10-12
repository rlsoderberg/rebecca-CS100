import sys
sys.path.append('../module3')

from _tuples import create_list

#grocery list confirmation is reinvogorated by file import combo
grocery_list = create_list()
#initialize lineno
lineno = 0
yes = ""
#loop through lines in text opened through file variable
for line in grocery_list:
    #strip lineno
    if lineno < 4:
        print(str(lineno)+": "+line.strip())
    elif lineno >= 4:
        print(line.strip())
    #question user about purchase decision
    if lineno < 4:
        while yes != 'y' or yes != 'Y':
            print("would you REALLY like to make this purchase?")
            #accept input
            yes = input()
    #advance lineno
    lineno = lineno + 1

grocery_list.close()



