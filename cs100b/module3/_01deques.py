import collections
import random

#lifesaver class stores flavor data
class Lifesaver:
    def __init__(self, flavor = ''):
        self.flavor = flavor

#function to build the tube
def rollgen():
    #deque is a collection that can be edited at both ends. remember that deque has parentheses
    #we are going to pop lifesavors from our tube deque
    tube = collections.deque()

    #list of lifesaver flavors
    flavors = ['orange', 'pineapple', 'cherry', 'pina colada', 'grape']
    #what, there's no grape???

    for l in range(0, 14):
        randint = random.randrange(0, 5)
        lifesaver = Lifesaver(flavors[randint])
        tube.append(lifesaver)

    return tube

#function to pop lifesavers
def rollpop(tube):
    #initialize popcount
    popcount = 1

    #loop until tube runs out
    while len(tube) > 0:
        #let user choose which side to pop
        side = input('from which side do you wish to pop - l or r? ')
        while side != 'l' and side != 'r':
            print('invalid input. l or r?')
        if side == 'l':
            #you COULD use the same variable for both pops, if you wanted to
            leftsaver = tube.popleft()
            print(f'lifesaver {popcount}. left side, {leftsaver.flavor}')
        elif side == 'r':
            rightsaver = tube.pop()
            print(f'lifesaver {popcount}. right side, {rightsaver.flavor}')
        #keep track of popcount, so you can make sure you have the right number of lifesavers...
        popcount = popcount + 1
    print('no lifesavers left!')
        
def main():
    tube = rollgen()
    rollpop(tube)

main()


