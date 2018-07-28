class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:
        nextnode = current.next_node

        current.next_node = previous

        previous = current
        current = nextnode

    return previous



a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c

reverse(a)
print(c.next_node.value)
print(b.next_node.value)
