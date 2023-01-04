import collections

class Stack:
    def __init__(self):
        self.deque = collections.deque()

    def push(self, item):
        self.deque.appendleft(item)

    def pop(self):
        return self.deque.popleft()
    
    def top(self):
        return self.deque[0]

    def len(self):
        return len(self.deque)

names = ['alice', 'bob', 'carol', 'dave', 'edith', 'fred']

stack = Stack()
for n in names:
    stack.push(n)

while stack.len() > 0:
    print(stack.top())
    stack.pop()