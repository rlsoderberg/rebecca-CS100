import sys
sys.path.append('../..')

from i import input_function

def total_calc(bill, tip):
    tip = bill * (0.01 * tip)
    total = bill + tip
    return total

print("select prob_num 1, 2, 3, or 4")
prob_num = 0
while prob_num != 1 and prob_num != 2 and prob_num != 3 and prob_num != 4:
    prob_num = int(input_function("int"))

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

    ans1 = round((int1 + 8),2)
    ans2 = round((float2 - int2),2)
    ans3 = round((int3 * float3),2)
    ans4 = round((float1 / 4),2)
    ans5 = round((int3 % int2),2)


    print("\n equations containing given variables:")
    print("int1 + 8 = "+str(ans1))
    print("float2 - int2 = " + str(ans2))
    print("int3 * float3 = "+ str(ans3))
    print("float1 / 4 = "+ str(ans4))
    print("int3 % int2 = "+str(ans5))

elif prob_num == 2:
    bill = 0
    print("what is your bill?")
    bill = float(input_function("int"))
    
    print("tip totals for a bill of $"+str(format(bill, ".2f"))+": 10%: "+str(format((total_calc(bill, 10)), ".2f"))+". 15%: "+str(format((total_calc(bill, 15)), ".2f"))+". 20%: "+str(format((total_calc(bill, 20)), ".2f"))+". 25%: "+str(format((total_calc(bill, 25)), ".2f"))+".")
    print("which tip percentage would you like to use?")
    print("10, 15, 20, or 25?")
    tip_select = ""
    while tip_select != 10 and tip_select != 15 and tip_select != 20 and tip_select != 25:
        tip_select = int(input_function("int"))
    print("congratulations! you have made a tip of %"+str(tip_select)+"!")
    total = bill +(bill*0.01*(int(tip_select)))
    print("your total is $"+str(format(total, ".2f")))



elif prob_num == 3:
    games = []
    for x in range (0, 5):
        game_no = x
        print("enter game total for game " + str(x+1))
        total = int(input_function("int"))
        games.append(total)
        x += 1

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