class DoublyLinkListNode(object):
    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = DoublyLinkListNode(1)
b = DoublyLinkListNode(2)
c = DoublyLinkListNode(3)

a.next_node = b
b.next_node = c

b.prev_node = a
c.prev_node = b

print(a.value)
print(b.prev_node.value)
print(a.next_node.value)
print(c.prev_node.value)
print(b.next_node.value)
