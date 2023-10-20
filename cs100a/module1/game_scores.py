#i'm doing the same thing for the 3rd problem of variables & userinput
#right, i'm also doing the second part of this problem
print('enter your game scores.')
scores = []
loopnumber = 1
exit = 0
while exit != "d":
    exit = input(f"enter score {loopnumber}, or enter d if done: ")
    if exit != "d":
        scores.append(int(exit))
    loopnumber += 1

#scores = [13, 18, 21, 17, 31]

#ooh, i'm trying to think if there is a good way to dynamically assign variable names in python
#what do you mean, store each of those point totals in separate variables (e.g. game1, game2, ...)?
#is there some good way to do that???