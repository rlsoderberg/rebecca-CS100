import random

#i won't TOTALLY restart, but i'll go over everything to make sure i remember it
#and this had better be the last time, since i'm labeling it 0...

#so here... we have the input function.
#i seemed to be using an int only input function last time. 
#since this is "math", right???
def int_input_function():
    valid = False
    while valid == False:
        try:
            x = int(input())
            if not x:
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  

#we are importing random so that we can randomize the problem sequence
#oh right, i just looked, and this is the one where i got way overly elaborate with the math volcano
#i'm going to try to get through pretty fast, so that i can conserve my precious bodily fluids

#array of equation strings
equation_strings = ["5x + 3 = 13", "14 - 3x = 2", "9 - 2x = 3", "8x + 2 = 50", "2x + 16 = 40", 
                    "12 - 2x = 2", "7 = 49 - 6x", "30 + 7x = 86", "4x + 20 = 56", "3x - 3 = 39"]
#array of answer ints
answers = [2, 4, 3, 6, 12, 5, 7, 8, 9, 14]
#right, i was thinking of coming up with a way to auto solve these
#might be kind of pointless??? i'm going more for the web stuff right now

#quick narration
print("You are climbing a mountain, and you find a doorway behind a rock.")

#handy dandy "while valid" loop!!!
valid = False
while valid == False:
    try:
        valid2 = False
        while valid2 == False:
            takeboat = str(input("Press a to enter the doorway: "))
            if takeboat in ("a"):
                valid2 = True
            else:
                print("Invalid input. Press a to enter the doorway: ")
        valid = True
    except:
        print("Invalid input. Press a to enter the doorway: ")

#well... i had to restart from here, due to some kind of error???
#i am working to eliminate the illusion of choice

print("You reach your hand toward the doorway. An alarm screeches out.")
print("A math problem materializes on the doorway.")

#random number
rando = 0
#array of random numbers
prob_seq = []
correct = 0

for x in range (0, 10):
    #oh right, i guess the question is pretty simple, 'randint inclusive'. 
    #not seeing a good simple answer anywhere, guess it doesn't matter that much
    rando = random.randint(0,9)
    while rando in prob_seq:
        rando = random.randint(0,9)
    prob_seq.append(rando)
    print(str(x + 1) + ": " + equation_strings[rando])
    user_ans = 0
    print("Input answer: ")
    user_ans = int_input_function()
    if int(user_ans) == answers[rando]:
        print("correct")
        correct += 1
    elif int(user_ans) != answers[rando]:
        print("incorrect")

print(str(correct) + " correct")
    
      

