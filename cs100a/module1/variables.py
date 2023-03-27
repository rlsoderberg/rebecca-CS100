int1 = 3
int2 = 5
int3 = 6
float1 = 1.2
float2 = 4.7
float3 = 6.5

print("int1 + 8 ="+str(round((int1 + 8),2)))
print("float2 - int2 = " + str(round((float2 - int2),2)))
print("int3 * float3 = "+ str(round(int3 * float3),2))
print("float1 / 4 = "+ str(round(float1/4),2))
print("int3 % int2 = "+str(round(int3%int2),2))

#at first it returned float2 - int2 = -0.2999999999999998 and i have nooo idea why
#but omg it doesn't like me turning rounds into strs and idk!!!!!!!!
