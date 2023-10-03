#so many files!!!
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

#i'm stealing the equation strings, and the answers, but i will type at least one so i remember how
equation_strings = ["5x + 3 = 13", "14 - 3x = 2", "9 - 2x = 3", "8x + 2 = 50", "2x + 16 = 40", 
                    "12 - 2x = 2", "7 = 49 - 6x", "30 + 7x = 86", "4x + 20 = 56", "3x - 3 = 39"]
answers = [2, 4, 3, 6, 12, 5, 7, 8, 9, 14]
#right, i was thinking of coming up with a way to auto solve these
#might be kind of pointless??? i'm going more for the web stuff right now

#quick narration
print("You are climbing a mountain, and you find a door behind a rock.")

#handy dandy "while valid" loop!!!
valid = False
while valid == False:
    try:
        valid2 = False
        while valid2 == False:
            takeboat = str(input("Will you enter the door? Press a to enter. Press b to climb away."))
            if takeboat in ("a", "b"):
                valid2 = True
            else:
                print("Invalid input. Please enter a or b: ")
        valid = True
    except:
        print("Invalid input. Please enter a or b: ")
#i'm trying to get it to print 'success', if takeboar is in ("a", "b")
#i tried to put this inside the loop, but it didn't work!
print("SUCCESS!")
#well now it's working. why did i have to put it outside?
#i mean i guess it's good not to have TOO much inside...

