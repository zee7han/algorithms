# It's a simple class for implement the singly link list node.
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

# Here we implement the function for reverse the link list.
def reverse(head):
    # Initiate the three pointer to keep track.
    current = head
    previous = None
    nextnode = None
    # Update the pointers till current element exists.
    while current:
        # Store the current next_node for future reference.
        nextnode = current.next_node
        # Update current node pointer with previous.
        current.next_node = previous
        # Update the previous as current node and current as next_node
        previous = current
        current = nextnode
    # Return the previous as head.
    return previous


# checking for our solution.
a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c

reverse(a)
print(c.next_node.value)
print(b.next_node.value)
