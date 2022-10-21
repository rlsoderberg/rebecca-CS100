#create blank array of average points
avg = []

#request user input of average points
print("Please enter average points for the last five games.")
for s in range(0,6):
    valid = False
    while valid == False:
        try:
            print("Average points for game ",s)
            avg.append(int(input()))
            valid = True
        except ValueError:
            print("Invalid input.")

#calculate megatotal of average points
megatotal = 0
for x in range (0, 5):
    megatotal += avg[x]

#calculate superaverage from megatotal
generalaverage = megatotal / 5

#print superaverage
print("The general average, the average of the given point averages, is ",generalaverage)