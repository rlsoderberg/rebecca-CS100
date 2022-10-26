user_status = input("How are you doing today? ")
array = user_status.split(" ")
print(array[0].upper(), "\n", array[0].upper(), "\n")
#catch if length of array is 0?
for s in array:
    #print(array[s].upper(), "\n")
    #print(array[int(s)].upper(), "\n")
    #print(s.upper(), "\n")
    s+=1