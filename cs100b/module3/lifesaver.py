import collections
import random

class LifeSaver:
    def __init__(self, flavor):
        self.flavor=flavor

import collections
import random

class LifeSaver:
    def __init__(self, flavor):
        self.flavor = flavor

tube = collections.deque()
flavors = ["orange","pineapple","cherry","raspberry","watermelon"]
for l in range (0,10):
    flavor = flavors[random.randrange(0,len(flavors))]
    lifesaver = LifeSaver(flavor)
    tube.append(lifesaver)

while len(tube)>0:
    side = random.randrange(0,2)
    if side ==0:
        l = tube.pop()
        print("eating " + l.flavor + " from the right side")
    else:
        l = tube.popleft()
        print("eating "+l.flavor+" from the left side")

print("YUM!")