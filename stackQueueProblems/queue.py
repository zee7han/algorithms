# Here we create a queue class
class Queue(object):
    # It initialize the empty queue
    def __init__(self):
        self.items = []
    # Check whether queue is empty or not
    def isEmpty(self):
        return self.items == []
    # Insert the element at first index or start of the queue
    def enqueue(self, item):
        self.items.insert(0, item)
    # Delete a element from the end of the queue
    def dequeue(self):
        return self.items.pop()
    # Returns the size of the queue
    def size(self):
        return len(self.items)

# Create the object of the queue class and test it various functions
q = Queue()

print(q.isEmpty())
print(q.enqueue("Hello"))
print(q.size())
print(q.isEmpty())
print(q.dequeue())
print(q.size())
print(q .isEmpty())
