import sys
sys.path.append('../..')

from i import input_function

#function for calculating total bill
def total_calc(bill, tip):
    tip = bill * (0.01 * tip)
    total = bill + tip
    return total

print("select prob_num 1, 2, or 3")
prob_num = 0
#limit problem selection to 1, 2, or 3
while prob_num != "1" and prob_num != "2" and prob_num != "3":
    prob_num = input()

#input function limits to int or float variables
if prob_num == 1:
    print("int1 = ")
    int1 = int(input_function("int"))
    print("int2 = ")
    int2 = int(input_function("int"))
    print("int3 = ")
    int3 = int(input_function("int"))
    print("float1 = ")
    float1 = float(input_function("float"))
    print("float2 = ")
    float2 = float(input_function("float"))
    print("float3 = ")
    float3 = float(input_function("float"))

    #print & calculate & round equations at the same time, if you can use the right number of parentheses
    print("\n equations containing given variables:")
    print("int1 + 8 = "+str(round((int1 + 8),2)))
    print("float2 - int2 = " + str(round((float2 - int2),2)))
    print("int3 * float3 = "+ str(round((int3 * float3),2)))
    print("float1 / 4 = "+ str(round((float1 / 4),2)))
    print("int3 % int2 = "+str(round((int3 % int2),2)))

elif prob_num == 2:
    bill = 0
    print("what is your bill? (in decimal values only)")
    bill = float(input_function("float"))
    
    #printing and calculating and rounding all at once to display possible tip totals
    print("tip totals for a bill of $"+str(format(bill, ".2f"))+": 10%: "+str(format((total_calc(bill, 10)), ".2f"))+". 15%: "+str(format((total_calc(bill, 15)), ".2f"))+". 20%: "+str(format((total_calc(bill, 20)), ".2f"))+". 25%: "+str(format((total_calc(bill, 25)), ".2f"))+".")
    print("which tip percentage would you like to use?")
    print("10, 15, 20, or 25?")
    tip_select = ""
    #user is limited to given tip totals
    while tip_select != "10" and tip_select != "15" and tip_select != "20" and tip_select != "25":
        tip_select = input()
    print("congratulations! you have made a tip of %"+tip_select+"!")
    total = bill +(bill*0.01*(int(tip_select)))
    print("your total is $"+str(format(total, ".2f")))



elif prob_num == 3:
    games = []
    #user enters point totals. they have to be in order!!
    for x in range (0, 5):
        game_no = x
        print("enter point total for game " + str(x+1))
        total = int(input_function("int"))
        games.append(total)
        x += 1

    #totaling up points and games. 'x in games' makes more sense now? i just had to get used to it?
    total_points = 0
    total_games = 0
    for x in games:
        total_points += x
        total_games += 1
        x += 1
    
    avg_points = total_points / total_games

    print("points for recent games: "+str(games))
    print("total points: "+str(total_points))
    print("average points per game: "+str(avg_points))