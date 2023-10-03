import random

player_wins = 0
comp_wins = 0
gameover = 0
#this is the correct order of rock paper scissors
rps_strings = ["rock","scissors", "paper"]
player_rps = 0
comp_rps = 0

#ooooooooh, i was accidentally fixing this one... yeah, i don't know
#i want to keep playing as long as the game is not over, so that should be on the outside
while rounds > 0:
    while player_rps != 1 and player_rps != 2 and player_rps!= 3:
        player_rps = int(input("1. rock, 2. scissors, or 3. paper? "))
    comp_rps = random.randint(1,3)
    if player_rps == comp_rps:
        print("you played "+rps_strings[player_rps-1]+" and computer played "+rps_strings[player_rps-1]+". it's a tie!")
    elif player_rps > comp_rps:
        print("you played "+rps_strings[player_rps-1]+" and computer played "+rps_strings[player_rps-1]+"! "+rps_strings[player_rps-1]+" beats rock! you win")
        player_wins += 1
    elif player_rps < comp_rps:
        print("you played "+rps_strings[player_rps-1]+" and computer played "+rps_strings[player_rps-1]+"! "+rps_strings[player_rps-1]+" beats rock! computer wins")
        comp_wins += 1
    player_rps = 0
    comp_rps = 0
    print("player wins: "+str(player_wins)+"   computer wins: "+str(comp_wins))
    if player_wins == 7:
        gameover = 1
    if comp_wins == 7:
        gameover = 1
    
#dictionary helps you check max between two variables!!
dict = {player_wins:"player",comp_wins:"computer"}
winner = dict.get(max(dict))
print("SCORE TOTALS\nplayer: "+str(player_wins)+"\ncomputer: "+str(comp_wins)+"\n"+winner+" wins!")



