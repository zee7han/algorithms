class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

def last_to_nth_node(n,head):
    left = head
    right = head

    for i in range(n):
        if not right.next_node:
            raise LookUpError("Error: n is larger than linked list")
        right = right.next_node

    while right.next_node:
        left = left.next_node
        right = right.next_node

    return left



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)


a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

result = last_to_nth_node(2,a)
print(result.value)
