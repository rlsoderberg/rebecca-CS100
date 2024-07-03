import collections

#we have to make our own stack!!! stack is like a stack of cans

class Stack():
    def __init__(self):
        self.deque = collections.deque()

    def push(self, can):
        #doing this without looking (although i kind of looked before)
        #this one must be... you put something on top.
        #where is the top??? it must be the place where it automatically comes out, the right???
        #i don't know if that's right
        #i think i saw left in there somewhere
        #maybe it's the opposite of the right
        
        #self.pushleft(can) i don't know what it is actually called when you do that!!!
        #oh, you first of all have to say deque, and then it's append
        self.deque.appendleft(can)

    def pop(self):
        #correctness!!!!!!!!
        self.deque.popleft()

    def top(self):
        #this one, you check what's on the top (yeah yeah, i did kind of look before)
        #self.deque.viewleft() how do you do this?????
        #oh, you do it with an array!!!!

        #DON'T FORGET THE DEQUE!!!
        return self.deque[0]
        #so, if the left is 0... then the right is the end??? so the deque automatically pops off the end???
        #so it's... kind of the opposite of a stack? a little bit? at least in spirit?


    def len(self):
        #this one's already in there!!!
        #return self.deque.len() that's not how you do it though!!! len comes first!!! len likes to give hugs!!!
        return len(self.deque)
        #awwww