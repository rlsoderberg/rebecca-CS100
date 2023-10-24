#deque lives in collection
import collections
import random

#we're using a lifesaver object, which basically allows us to make a collection of strings
class LifeSaver():
    #lifesaver object is all about flavor
    def __init__(self, flavor):
        self.flavor = flavor
    
#rollgen function generates a roll of randomly flavored lifesavers
def rollgen():
    roll = collections.deque()
    #use list of strings, not one long string, which returns flavors 1 character long
    flavors = ['watermelon', 'cherry', 'pineapple', 'raspberry', 'orange']
    for f in range(1, 11):
        #random flavor out of all the flavors, no matter how many flavors there are
        flavor = flavors[random.randrange(0, len(flavors))]
        #create lifesaver object with given flavor
        lifesaver = LifeSaver(flavor)
        #store lifesaver in roll
        roll.append(lifesaver)
    return roll

#remove function takes lifesaver out of roll and prints results
def remove(roll, side):
    #our roll of lifesavers is finite, and our program reflects this with a while loop
    while len(roll) > 0:
        if side == 'l':
            s = roll.popleft()
            #it is good to refer directly to the flavor attribute, instead of trying to make a variable for it
            print(f'eating {s.flavor} lifesaver from the left side ')
        elif side == 'r':
            s = roll.pop()
            print(f'eating {s.flavor} lifesaver from the right side ')
    print('you finished the roll of life savers!')

def main():
    #initialize exit
    exit = ''
    #run the rollgen function
    roll = rollgen()
    while exit != 'x':
        #initialize side
        side = ''
        while side != 'l' and side != 'r':
            #you are only allowed to remove from one side for the entire roll 
            side = input('what side do you want to remove from, l or r?')
        #run the remove function
        remove(roll, side)
        exit = input('press any key to continue, or x to exit')

main()
