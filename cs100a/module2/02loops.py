import random

print("which problem do you want to do? 1 or 2?")
problem = 0
while problem != "1" and problem != "2":
    problem = input()

if problem == "1":
    print("1. rock, 2. scissors, or 3. paper?")
    rps_strings = ["rock","scissors", "paper"]
    player_rps = 0
    comp_rps = 0
    while player_rps == comp_rps:
        while player_rps != 1 and player_rps != 2 and player_rps!= 3:
            player_rps = int(input())
        comp_rps = random.randint(1,3)
        if player_rps == comp_rps:
            print("you played "+rps_strings[player_rps-1]+" and computer played "+rps_strings[player_rps-1]+". it's a tie!")
        elif player_rps == 3 and comp_rps == 1:
            print("you played paper and computer played rock! paper beats rock! you win")
        elif player_rps == 1 and comp_rps == 3:
            print("you played rock and computer played paper! paper beats rock! computer wins")
        elif player_rps < comp_rps:
            print("you played "+rps_strings[player_rps-1]+" and computer played "+rps_strings[comp_rps-1]+"! "+rps_strings[player_rps-1]+" beats "+rps_strings[comp_rps-1]+"! you win")
        elif player_rps > comp_rps:
            print("you played "+rps_strings[player_rps-1]+" and computer played "+rps_strings[comp_rps-1]+"! "+rps_strings[comp_rps-1]+" beats "+rps_strings[player_rps-1]+"! computer wins")
            player_rps = 0
            comp_rps = 0

elif problem == "2":
    print("hello")



