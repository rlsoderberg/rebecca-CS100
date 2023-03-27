import sys
sys.path.append('../..')

from i import input_function

print("select prob_num 1, 2, or 3")
type_name = "int"
prob_num = 0
while prob_num != 1 and prob_num != 2 and prob_num != 3:
    prob_num = int(input_function(type_name))

int1 = 3
int2 = 5
int3 = 6
float1 = 1.2
float2 = 4.7
float3 = 6.5

ans1 = round((int1 + 8),2)
ans2 = round((float2 - int2),2)
ans3 = round((int3 * float3),2)
ans4 = round((float1 / 4),2)
ans5 = round((int3 % int2),2)

if prob_num == 1:
    print("\n equations containing int1, int2, int3, float1, float2, and float3:")
    print("int1 + 8 = "+str(ans1))
    print("float2 - int2 = " + str(ans2))
    print("int3 * float3 = "+ str(ans3))
    print("float1 / 4 = "+ str(ans4))
    print("int3 % int2 = "+str(ans5))

#at first it returned float2 - int2 = -0.2999999999999998 and i have nooo idea why
#but omg it doesn't like me turning rounds into strs and idk!!!!!!!!

#ok fine, for now i'm copy pasting. probably could have worked somehow?

elif prob_num == 2:
    bill = 47.56
    print("your bill is $", bill, ".")
    print("how much do you want to tip?")
    print("please enter 10, 15, 20, or 25")
    type_name = "int"
    x = 0
    while x != 10 and x != 15 and x != 20 and x != 25:
        x = int(input_function(type_name))

    tip = bill * (0.01 * x)
    total = bill + tip

    print(x,"% tip on bill of $",format(bill, '.2f'),"is $",format(tip, '.2f')," and total is $",format(total,'.2f'))


elif prob_num == 3:
    games = [13, 18, 21, 17, 31]

    total_points = 0
    total_games = 0
    #i swear!!! python is so weird like this!!! look what i did the first time i did this problem:
    """
    for x in range (0, 5):
        megatotal += games[x]
    """
    #but it didn't let me do that with 'x in games'!!! aaaaaaaaaa
    for x in games:
        total_points += x
        total_games += 1
        x += 1
    
    avg_points = total_points / total_games

    #all these strs!!! literally what is this!!!
    print("points for recent games: "+str(games))
    print("total points: "+str(total_points))
    print("average points per game: "+str(avg_points))


    
