import random

import sys
sys.path.append("../..")

from i import int_input_function

player_wins = 0
comp_wins = 0

rps_strings = [0, "rock","paper", "scissors"]
player_rps = 0
comp_rps = 0

print("How many rounds do you want to play? Please enter any integer: ")
rounds = int_input_function()

while rounds > 0:
    player_rps = 0
    comp_rps = 0
    winner = ""
    
    while player_rps != 1 and player_rps != 2 and player_rps != 3:
        player_rps = input("\n1. Rock, 2. Paper, or 3. Scissors?")

    #now... can i convert this to f strings?

    #oh, fiddlesticks! rps is so particular!
    comp_rps = random.randint(0,3)

    print(f"you played {rps_strings[player_rps]} and computer played {rps_strings[comp_rps]}.")

    if comp_rps == 1:
        if player_rps == 2:
            winner = "p"
        elif player_rps == 3:
            winner = "c"
    elif comp_rps == 2:
        if player_rps == 1:
            winner = "c"
        elif player_rps == 3:
            winner = "p"
    elif comp_rps == 3:
        if player_rps == 1:
            winner = "p"
        elif player_rps == 2:
            winner = "c"

    if winner == "":
        print("it's a tie!")
    elif winner == "p":
        print(f"{rps_strings[player_rps]} beats {rps_strings[comp_rps]}! you win")
        player_wins += 1
    elif winner == "c":
        print(f"{rps_strings[comp_rps]} beats {rps_strings[player_rps]}! computer wins")
        comp_wins += 1
    print(f"player wins: {player_wins}   computer wins: {comp_wins}")

    if player_rps != comp_rps:
        rounds -= 1
    
#dictionary helps you check max between two variables!!
dict = {player_wins:"player",comp_wins:"computer"}
winner = dict.get(max(dict))
print("SCORE TOTALS\nplayer: "+str(player_wins)+"\ncomputer: "+str(comp_wins)+"\n"+winner+" wins!")