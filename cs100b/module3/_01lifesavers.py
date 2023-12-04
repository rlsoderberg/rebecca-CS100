import collections
import random

#lifesaver class stores flavor data
#oh wait, class needs parentheses!!! why was this working?
class Lifesaver():
    def __init__(self, flavor = ''):
        self.flavor = flavor

#function to generate tube of lifesavers
def tubegen():
    #deque is a collection that can be edited at both ends. remember that deque has parentheses
    tube = collections.deque()

    #list of lifesaver flavors
    flavors = ['orange', 'pineapple', 'cherry', 'raspberry', 'watermelon']

    #make the whole roll of lifesavers
    for l in range(0, 14):
        #whoa! now there's a shortcut, random.choice!
        flavor = random.choice(flavors)
        lifesaver = Lifesaver(flavor)
        tube.append(lifesaver)

    return tube

#function to eat lifesavers from each end
def tubepop(tube):
#initialize popcount
    popcount = 1

    #loop until tube runs out
    while len(tube) > 0:
        #randomly choose side
        side = random.randrange(0,2)
        if side == 0:
            s = tube.popleft()
            print(f'lifesaver {popcount}. left side, {s.flavor}')
        elif side == 1:
            s = tube.pop()
            print(f'lifesaver {popcount}. right side, {s.flavor}')
        #keep track of popcount, so you can make sure you have the right number of lifesavers...
        popcount = popcount + 1
    print('no lifesavers left!')

def main():
    tube = tubegen()
    tubepop(tube)

main()

