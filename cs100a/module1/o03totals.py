#where is this problem? i literally don't even know what i'm doing right now

#create array of games
games = [13, 18, 21, 17, 31]

game_total = len(games)


#display array of averages to user
print("Diana's average points in the last"+str(game_total)+" games are ",str(games))

#increment megatotal by each of the point averages
megatotal = 0
for x in range (0, 5):
    megatotal += games[x]

#print megatotal
print("Diana's megatotal, the sum of these point averages, is ",str(megatotal))

mega_average = megatotal / game_total

print("Diana's mega_average, over all games, is "+str(mega_average))
