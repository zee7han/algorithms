# Here implement the stack using the python list.
class Stack(object):
    # Initialize the empty stack on creation of object.
    def __init__(self):
        self.items = []
    # Check the stack is empty or not.
    def isEmpty(self):
        return self.items == []
    #Push an element on the top of stack.
    def push(self, item):
        self.items.append(item)
    # Pop the element from top of the stack.
    def pop(self):
        return self.items.pop()
    # Find the top element of the stack.
    def peek(self):
        return self.items[len(self.items)-1]
    # Give the size of the list.
    def size(self):
        return len(self.items)


s = Stack()

print(s.isEmpty())
print(s.push("Hello"))
print(s.peek())
print(s.size())
print(s.isEmpty())
print(s.pop())
print(s.size())
print(s.isEmpty())
