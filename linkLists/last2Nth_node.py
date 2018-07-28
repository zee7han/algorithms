# It's a simple class for implement the singly link list node.
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

# Here is implementation of finding nth node from last in singly linked list.
def last_to_nth_node(n,head):
    # Initiate two pointers left, right point to start.
    left = head
    right = head
    # Here we increase the right pointer till n times to reach nth node from start.
    for i in range(n):
        # check for edge case if link list is smaller than n.
        if not right.next_node:
            raise LookUpError("Error: n is larger than linked list")
        # Otherwise update the right pointer.
        right = right.next_node
    # Here we update the both pointer by next_node if right pointer next_node
    # exists and at last left pointer will be at position of nth element from
    # the last.
    while right.next_node:
        left = left.next_node
        right = right.next_node

    return left


# checking for our solutions.
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
