from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def getSize(self):
        return len(self.buffer)

pq = Queue()
pq.enqueue("hello")
pq.enqueue("bye")
pq.enqueue("again")
print(pq.getSize())
print(pq.dequeue()) 