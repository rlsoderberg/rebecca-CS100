#request user input for length of panda list
w = False
while w == False:
    try:
        panda = int(input("how many panda?"))
        if panda == "":
            raise ValueError('empty string')
        w = True
    except ValueError:
        print("invalid Input")

#introduce panda request loop
print(f'i will ask of you {panda} panda')

#initialize list of int pandas
#if you haven't learned about lists yet, free range variables would also work
pandalist = []

#int input function
print("note: pandas must be integers")
for x in range (0, panda):
    w = False
    while w == False:
        try:
            newpanda = int(input(f'panda {x+1}: '))
            if newpanda == "":
                raise ValueError('empty string')
            pandalist.append(newpanda)
            w = True
        except ValueError:
            print("invalid Input")
    x+=1

#perform operation
print("problem 1. modulo ") 
print(f"panda 1 % panda 3 = {pandalist[0] % pandalist[-1]}") 
