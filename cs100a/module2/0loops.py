import random

import sys
sys.path.append("../..")

from i import int_input_function

player_wins = 0
comp_wins = 0
gameover = 0

rps_strings = ["rock","scissors", "paper"]
player_rps = 0
comp_rps = 0

print("How many rounds do you want to play? Please enter any integer: ")
rounds = int_input_function()

while rounds > 0:
    print("1. Rock, 2. Paper, or 3. Scissors?")
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
    comp_rps = random.randint(1,3)
    if player_rps == comp_rps:
        print("you played "+rps_strings[player_rps]+" and computer played "+rps_strings[player_rps]+". it's a tie!")
    elif player_rps > comp_rps:
        print("you played "+rps_strings[player_rps]+" and computer played "+rps_strings[player_rps]+"! "+rps_strings[player_rps]+" beats "+rps_strings[player_rps]+"! you win")
        player_wins += 1
    elif player_rps < comp_rps:
        print("you played "+rps_strings[player_rps]+" and computer played "+rps_strings[player_rps]+"! "+rps_strings[player_rps]+" beats "+rps_strings[player_rps]+"! computer wins")
        comp_wins += 1
    player_rps = 0
    comp_rps = 0
    print("player wins: "+str(player_wins)+"   computer wins: "+str(comp_wins))
    if player_wins == 7:
        gameover = 1
    if comp_wins == 7:
        gameover = 1
    rounds -= 1
    
#dictionary helps you check max between two variables!!
dict = {player_wins:"player",comp_wins:"computer"}
winner = dict.get(max(dict))
print("SCORE TOTALS\nplayer: "+str(player_wins)+"\ncomputer: "+str(comp_wins)+"\n"+winner+" wins!")



