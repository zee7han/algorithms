class Dequeue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pushFront(self, item):
        self.items.insert(0,item)

    def popFront(self):
        return self.items.pop(0)

    def pushRear(self, item):
        self.items.append(item)

    def popRear(self):
        return self.items.pop()

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
