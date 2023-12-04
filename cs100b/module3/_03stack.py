import collections

#stack goes in opposite direction of deque, basically
class Stack:
    #we don't have to initialize deque... because it's internal, or whatever
    def __init__(self):
        self.deque = collections.deque()
    
    def push(self, item):
        self.deque.appendleft(item)

    def pop(self):
        #don't forget to return the things!
        return self.deque.popleft()

    def top(self):
        #deque seems to be indexable
        return self.deque[0]

    def len(self):
        return len(self.deque)

def main(): 
    names = ['alice', 'bob', 'carol', 'dave', 'edith', 'fred']
    stack = Stack()
    for n in names:
        stack.push(n)

    for n in names:
        print(stack.top())
        stack.pop()

main()



    