import random

player_wins = 0
comp_wins = 0
gameover = 0

rps_strings = ["rock","scissors", "paper"]
player_rps = 0
comp_rps = 0

#i want to keep playing as long as the game is not over, so that should be on the outside
while gameover == 0:
    while player_rps != 1 and player_rps != 2 and player_rps!= 3:
        player_rps = int(input("1. rock, 2. scissors, or 3. paper? "))
    comp_rps = random.randint(1,3)
    if player_rps == comp_rps:
        print("you played "+rps_strings[player_rps-1]+" and computer played "+rps_strings[player_rps-1]+". it's a tie!")
    elif player_rps == 3 and comp_rps == 1:
        print("you played paper and computer played rock! paper beats rock! you win")
        player_wins += 1
    elif player_rps == 1 and comp_rps == 3:
        print("you played rock and computer played paper! paper beats rock! computer wins")
        comp_wins += 1
    elif player_rps < comp_rps:
        print("you played "+rps_strings[player_rps-1]+" and computer played "+rps_strings[comp_rps-1]+"! "+rps_strings[player_rps-1]+" beats "+rps_strings[comp_rps-1]+"! you win")
        player_wins += 1
    elif player_rps > comp_rps:
        print("you played "+rps_strings[player_rps-1]+" and computer played "+rps_strings[comp_rps-1]+"! "+rps_strings[comp_rps-1]+" beats "+rps_strings[player_rps-1]+"! computer wins")
        comp_wins += 1
    player_rps = 0
    comp_rps = 0
    print("player wins: "+str(player_wins)+"   computer wins: "+str(comp_wins))
    if player_wins == 7:
        gameover = 1
    if comp_wins == 7:
        gameover = 1

dict = {player_wins:"player",comp_wins:"computer"}
winner = dict.get(max(dict))
print("SCORE TOTALS\nplayer: "+str(player_wins)+"\ncomputer: "+str(comp_wins)+"\n"+winner+" wins!")



