# Here we are implementing the queue using the 2 stacks.
class Queue2Stacks(object):
    # initialize the two stacks.
    def __init__(self):
        self.inStack = []
        self.outStack = []
    # Insert the element in inStack.
    def enqueue(self,item):
        self.inStack.append(item)
    # Delete the element by doubly reversing the order of element of the inStack.
    def dequeue(self):
        # Check if outStack is empty.
        if not self.outStack:
            # Loop through inStack till all elements are pop.
            while self.inStack:
                # Append the pop element of the inStack into the outStack.
                self.outStack.append(self.inStack.pop())
        # Pop the element from the outStack and return it.
        return self.outStack.pop()

queue = Queue2Stacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)


print(queue.dequeue())
print(queue.dequeue())
