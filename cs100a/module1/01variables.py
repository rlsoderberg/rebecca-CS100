import sys
sys.path.append('../..')

from i import input_function

print("select prob_num 1, 2, or 3")
x = 0
#um, is stuff that i deletedfrom i what made it an int? greeeat, i will have to retrieve those
while x != 1 and x != 2 and x != 3:
    x = input_function(int)
    print(x)

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

if x == 1:
    print("int1 + 8 = "+str(ans1))
    print("float2 - int2 = " + str(ans2))
    print("int3 * float3 = "+ str(ans3))
    print("float1 / 4 = "+ str(ans4))
    print("int3 % int2 = "+str(ans5))

#at first it returned float2 - int2 = -0.2999999999999998 and i have nooo idea why
#but omg it doesn't like me turning rounds into strs and idk!!!!!!!!

#ok fine, for now i'm copy pasting. probably could have worked somehow?

elif x == 2:
    bill = 0
    print("your bill is $", bill, ".")
    print("how much do you want to tip?")
    print("please enter 10, 15, 20, or 25")
    #dude, is type_name even necessary right now? i mean with int i guess it technically COULD be... 
    type_name = "int"
    x = 0
    while x != 10 and x != 15 and x != 20 and x != 25:
        x = input_function(type_name)

    tip = bill * (0.01 * x)
    total = bill + tip

    print(x,"% tip on bill of $",format(bill, '.2f'),"is $",format(tip, '.2f')," and total is $",format(total,'.2f'))

    #now it's stuck in a loop, UGH YES


    
