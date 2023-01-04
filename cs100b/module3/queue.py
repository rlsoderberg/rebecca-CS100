import collections

class Queue:
    def __init__(self):
        self.deque = collections.deque()

    def push(self, item):
        self.deque.append(item)
    
    def pop(self):
        return self.deque.popleft()

    def front(self):
        return self.deque[0]

    def len(self):
        return len(self.deque)