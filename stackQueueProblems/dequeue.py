# Here we initialize the class for implemetation of the dequeue.
class Dequeue(object):
    # Here initialze the empty dequeue.
    def __init__(self):
        self.items = []
    # This function checks whether the dequeue is empty or not.
    def isEmpty(self):
        return self.items == []
    # This function push element at the start of dequeue.
    def pushFront(self, item):
        self.items.insert(0,item)
    # This function delete the element from start of the dequeue.
    def popFront(self):
        return self.items.pop(0)
    # This function element at the last of dequeue.
    def pushRear(self, item):
        self.items.append(item)
    # This function delete element from the last of the dequeue.
    def popRear(self):
        return self.items.pop()
    # This function returns the size of the dequeue.
    def size(self):
        return len(self.items)

d = Dequeue()

print(d.isEmpty())
print(d.pushFront("At Start"))
print(d.pushRear("At End"))
print(d.isEmpty())
print(d.size())
print(d.popFront())
print(d.popRear())
print(d.isEmpty())
