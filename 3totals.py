#create array of average points
avg = [13, 18, 21, 17, 31]

#display array of averages to user
print("Diana's average points in the last 5 games are ",avg)

#increment megatotal by each of the point averages
megatotal = 0
for x in range (0, 5):
    megatotal += avg[x]

#print megatotal
print("Diana's megatotal, the sum of these point averages, is ",megatotal)