problem = ""
while problem != "1" and problem != "2" and problem != "3":
    problem = input("do you wish to view problem: 1. team sort 2. in keyword ? ")
    
quit = ""
while quit != "q":

    if problem == "1":
        team = []
        player = ""

        while player != "done":
            player = input("input player name, and enter 'done' when finished: ")
            if player != "done":
                team.append(player)

        team.sort()
        print("player list in alphabetical order: "+str(team))

    elif problem == "2":
        team = []
        player = ""

        while player != "done":
            player = input("input player name, and enter 'done' when finished: ")
            if player != "done":
                team.append(player)

        name = input("what is your name? ")
        if name in team:
            print("I can't wait to play")
        elif name not in team:
            print("Put me in coach, I'm ready to play.")

    quit = input("press m to return to problem menu, and q to quit")
