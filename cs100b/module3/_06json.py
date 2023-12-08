import json
import random
import collections
import datetime

class Lifesaver():
    def __init__(self, flavor):
    #i have to finish this!!! so now we're loading FROM json...
    #that is cool, you can check the type of an argument???
    #also, i don't really get what's going on here!!! how is this useful?
    #i don't get how that update method is working!!!
    #apparently that's just a thing you can do with class dictionaries?
        if type(flavor) is dict:
            self.__dict__.update()
        else:
            self.flavor = flavor

    #convert lifesaver object to json
    def toJson(self):
        return self.__dict__
    
#list of lifesaver objects
lifesavers = []

#deque of lifesavers
tube = collections.deque()

#what, do i not include 'r' if we're reading with json??
f = open('tube.json')
#ok, loads and dumps. json is a dumptruck
lifesavers = json.loads(f.read())
f.close()
for l in lifesavers:
    tube.append(Lifesaver(l))
    print(l)




#this stuff was under tube == collections.deque, for writing to json
"""
#i'm copying this in from lifesavers, because it seems like it might want to go here
flavors = ['orange', 'pineapple', 'cherry', 'raspberry', 'watermelon']

#for loop to make tube of lifesavers
for l in range(0, 14):
    flavor = random.choice(flavors)
    lifesaver = Lifesaver(flavor)
    tube.append(lifesaver)

#now we are making a tube of lifesaver dicts
lifesavers = []

#the point is im not sure what was wrong with it but this is a pastey version
for l in tube:
    #convert lifesavers object to dictionary so we can then convert it to json
    #right, so i was just looking at this like, why are we not just using __dict__ instead of toJson?
    #it... SEEMS to have the same result?
    #lifesavers.append(l.__dict__)
    #i mean, i guess i'll use the function, officially???
    lifesavers.append(l.toJson())

#i'm NOT including datetime, because that might be messing up my read...
#now = datetime.datetime.now()

f = open('tube.json', 'w')
f.write(str(now) + '\n')
#so that's the weird things that happen with json? you take a dict and dump it?
f.write(json.dumps(lifesavers))
f.close()
"""

