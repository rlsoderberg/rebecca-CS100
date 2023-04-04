#problem menu
problem = ""
while problem != "1" and problem != "2" and problem != "3":
    problem = input("do you wish to view problem: 1. team sort 2. in keyword ? ")
#don't quit until q   
quit = ""
while quit != "q":

    if problem == "1":
        #list of players, player variable
        team = []
        player = ""
        #get user to input player name, unless they're done
        while player != "done":
            player = input("input player name, and enter 'done' when finished: ")
            if player != "done":
                team.append(player)
        #sort team in alphabetical order and print
        team.sort()
        print("player list in alphabetical order: "+str(team))

    elif problem == "2":
        #list of players, player variable
        team = []
        player = ""

        #get user to input player name, unless they're done
        while player != "done":
            player = input("input player name, and enter 'done' when finished: ")
            if player != "done":
                team.append(player)
                
        #get user to input their own name, and see if it matches any of the player names
        name = input("what is your name? ")
        if name in team:
            print("I can't wait to play")
        elif name not in team:
            print("Put me in coach, I'm ready to play.")

    quit = input("press m to return to problem menu, and q to quit")
