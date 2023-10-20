#oh, i am totally regretting this restart!!! i mean, i know how to all this early stuff, right???
#i guess it might be helpful later, considering how bady my memory is
#selective do overs would probably be better, along with taking more notes!!!
#well, i need to go find a notebook, if i'm going to take notes
#this one i know though, right? variable assignment is pretty straightforward? so i can probably start now

#right, so what is actually the best way to make an int variable? you could int input, or you could convert later
#panda = int(input("how many panda?"))
#now this, of course, gives us an easy opportunity for error, unless we safeguard the input
""" look, this is my first attempt... 
w = False
while w == False:
    try:
        panda = input("how many panda?")
        if type(panda) != int:
            raise ValueError('empty string')#i forget how to say this... oh, RAISE ValueError
            w = True
    except:
        ValueError
"""
#so the problem here, is it just keeps asking, no matter what you say
#oh this is annoying, when i try to ctrl+c quit the program, it just keeps asking!!!! 
#well that last one was ridiculous, i just remembered that type error takes care of itself
#and what i'm actually asking in there is about emptry string (duhhh)

#properly, this should be down below
#no wait, this has to be up here also to get panda

w = False
while w == False:
    try:
        panda = int(input("how many panda?"))
        if panda == "":
            raise ValueError('empty string')
        w = True
    except ValueError:
        print("invalid Input")


print(f'i will ask of you {panda} panda')
#right, so it's official. range is weirdly inclusive, like, if you tell it (0, 6)...
#then it includes 0, but not 6? what even is that? 
#like, it includes 0, because it's like, hmmm, i'm a range, i'm going to start exactly where you tell me
#but then it's like, no, just kidding, i'm... i don't even know how to explain this one.
#i look at the range (0, 6), and i think, that must have either 7 or 5 values
#depending on whether or not it is inclusive 

pandalist = []
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

print("problem 1. modulo ") 
print(f"panda 1 % panda 3 = {pandalist[0] % pandalist[-1]}") 
print('you should be glad that pandas are integers, otherwise this might not have worked')

print('do you want to see?\n')
#(this is all too much)

w = False
while w == False:
    try:
        panda = int(input("how many panda?"))
        if panda == "":
            raise ValueError('empty string')
        w = True
    except ValueError:
        print("invalid Input")


print(f'i will ask of you {panda} panda')
#right, so it's official. range is weirdly inclusive, like, if you tell it (0, 6)...
#then it includes 0, but not 6? what even is that? 
#like, it includes 0, because it's like, hmmm, i'm a range, i'm going to start exactly where you tell me
#but then it's like, no, just kidding, i'm... i don't even know how to explain this one.
#i look at the range (0, 6), and i think, that must have either 7 or 5 values
#depending on whether or not it is inclusive 

pandalist = []
print("note: pandas must be floats")
for x in range (0, panda):
    w = False
    while w == False:
        try:
            newpanda = float(input(f'panda {x+1}: '))
            if newpanda == "":
                raise ValueError('empty string')
            pandalist.append(newpanda)
            w = True
        except ValueError:
            print("invalid Input")
    x+=1

print("problem 1. modulo ") 
print(f"panda 1 % panda 3 = {pandalist[0] % pandalist[-1]}") 

print('\nwell, it worked, but it might have given you a messy answer')
if len(str(pandalist[0] % pandalist[-1])) >= 5:
    print("that was pretty messy, wasn't it?")
else:
    print('but it looks like you got lucky this time...')


"""def int_input_function():
    valid = False
    while valid == False:
        try:
            x = int(input())
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  """

#well, i'm still getting the same problem!!! 
#oh, the indentation of w = True, THAT didn't help... fixed that...
#there we go!!! it's always indentation, isn't it??? 
#also, we need to put except ValueError on one line, and then put an error message

#right, so i'm comparing it closely now to the input function i had... if not x!!! does it mean the same thing?
#kind of looks like it does?

#oh, i get it i get it!!! that's why int(input()) is there, to raise a ValueError!!!
    
#what?? python complains when i try to convert a string into an int. come on!!! that was going to be fun times!!!

#well, anyway, that was good? i at least refreshed my memory on why the int input is there?
#see, i have such a hard time remembering things, so it's like, is this all pointless anyway???
#oh well, that was worth looking at the input function, i guess 
