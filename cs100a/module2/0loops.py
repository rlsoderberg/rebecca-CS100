import random

import sys
sys.path.append("../..")

from i import int_input_function

player_wins = 0
comp_wins = 0

rps_strings = [0, "rock","paper", "scissors"]
player_rps = 0
comp_rps = 0

print("Rcck Paper Scissors Tournament")
print("How many rounds do you want to play? Please enter any integer: ")
rounds = int_input_function()

while rounds > 0:
    player_rps = 0
    comp_rps = 0
    winner = ""
    
    print("\n1. Rock, 2. Paper, or 3. Scissors?")
    valid = False
    while valid == False:
        try:
            player_rps = int(input("Please enter 1, 2, or 3: "))
            if player_rps not in range (0, 4):
                raise ValueError("out of range")
            else:
                valid = True
        except ValueError:
            print("Invalid Input!")

    #now... can i convert this to f strings?

    #oh, fiddlesticks! rps is so particular!
    comp_rps = random.randint(1,3)

    print(f"you played {player_rps}.{rps_strings[player_rps]} and computer played {comp_rps}.{rps_strings[comp_rps]}.")

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
print("\nSCORE TOTALS\nplayer: "+str(player_wins)+"\ncomputer: "+str(comp_wins)+"\n"+winner+" wins the tournament!")