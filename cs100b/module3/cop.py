import json
import collections
import os
import random

class LifeSaver:
    def __init__(self, flavor):
        if type(flavor) is dict:
            self.__dict__.update(flavor)
        else:
            self.flavor = flavor
    def toJson(self):
        return self.__dict__

lifesavers = []
if os.access('tube.json', os.F_OK | os.R_OK | os.W_OK):
    f = open('tube.json')
    #read in the list of dictionary lifesavers
    lifesavers = json.loads(f.read())
    f.close()
    FLAVORS = open("tube.json", "r").read().split("\n")
    print(FLAVORS)

tube = collections.deque()
flavors = ["orange","pineapple","cherry","raspberry","watermelon"]
for l in range (0,10):
    flavor = flavors[random.randrange(0,len(flavors))]
    lifesaver = LifeSaver(flavor)
    tube.append(lifesaver)

for l in lifesavers:
    #since l is a dictionary, we can create a LifeSaver object from it
    tube.append(LifeSaver(l))

lifesavers = []
for l in tube:
    #convert the LifeSavers object to a Dictionary so we can convert it to JSON
    lifesavers.append(l.toJson())

f = open('tube.json', 'w')
f.write(json.dumps(lifesavers))
f.close()