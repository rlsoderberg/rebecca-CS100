#oh!!! we are making a class!!!
class Mento:
    def __init__(self, flavor):
        self.flavor = flavor

#deque lives in collections
import collections
import random

#flavors of fruit mentos
flavors = ['strawberry', 'orange', 'lemon']

#oh, i originally put fruit_mentos = [], but we're making this a deque, right!!!
tube = collections.deque()

#i tried to write this without looking and i forgot 'range', both with the for loop, and random
for x in range (1, 14):
    #you can put the random inside of flavors!!!
    flavor = flavors[random.randrange(0, len(flavors))]
    mento = Mento(flavor)
    tube.append(mento)
    
#eating the mentos
while len(tube) > 0:
    side = random.randrange(0, 2)
    if side == 0:
        #undirected pop is right!!!
        p = tube.pop()
        print(f"eating {p.flavor} from the right side")
    elif side == 1:
        p = tube.popleft()
        print(f"eating {p.flavor} from the left side")

print("YUM!")