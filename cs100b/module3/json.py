import json
import collections
import random

#you totally misspelled deque in the json section >:O >:O >:O

#wait, is EACH lifesaver object a dictionary? i am so confused

class LifeSaver:
    def __init__(self, flavor):
        self.flavor = flavor
    def toJson(self):
        return self.__dict__

#does this belong here???
tube = collections.deque()
flavors = ["orange","pineapple","cherry","raspberry","watermelon"]
for l in range (0,10):
    flavor = flavors[random.randrange(0,len(flavors))]
    lifesaver = LifeSaver(flavor)
    tube.append(lifesaver)

lifesavers = []
#what is tube???
for l in tube:
    lifesavers.append(l.toJson())

#i don't get this!!!! i see people doing it with 'with open'...
#ok, it says i am probably doing a circular import so i am stopping there because that sounds kind of fun
with open('tube.json', 'w') as f:
    json.dumps(lifesavers, f)
    f.close()