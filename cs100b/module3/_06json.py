import json
import random
import collections
import datetime

class Lifesaver():
    def __init__(self, flavor):
        self.flavor = flavor

    #convert lifesaver object to json
    def toJson(self):
        return self.__dict__
    
#list of lifesaver objects
lifesavers = []

#deque of lifesavers
tube = collections.deque()

#i'm copying this in from lifesavers, because it seems like it might want to go here
flavors = ['orange', 'pineapple', 'cherry', 'raspberry', 'watermelon']

#make the whole roll of lifesavers
for l in range(0, 14):
    #whoa! now there's a shortcut, random.choice!
    flavor = random.choice(flavors)
    lifesaver = Lifesaver(flavor)
    tube.append(lifesaver)

lifesavers = []

#so i tried to cobble together this thing really fast while i was writing, because it had errors...
for l in tube:
    #convert lifesavers object to dictionary so we can then convert it to json
    lifesavers.append(l.toJson())

#i'm including datetime, just to make sure my program is actually working
now = datetime.datetime.now()

f = open('tube.json', 'w')
f.write(str(now) + '\n')
#json comes through with vivid wordage of textformat.dumps
f.write(json.dumps(lifesavers))
f.close()

