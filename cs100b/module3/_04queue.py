import collections

#queue only pushes at the back. once again, front is left
class Queue():
    def __init__(self):
        self.deque = collections.deque()

    def push(self, item):
        self.deque.append()

    def pop(self):
        return self.deque.popleft()
    
    #queue has a front, while stack has a top
    def front(self):
        return self.deque[0]
    
    def len(self):
        return len(self.deque)
    

