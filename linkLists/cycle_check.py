# It's a simple node class for creating the Link list nodes.
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


# Here we implement the function for checking cycle in singly linked list.
def check_cycle(node):
    # Initiate the two marker or pointers.
    marker1 = node
    marker2 = node
    # we assume that the marker1 increased by 1 and marker2 run faster than
    # marker1 so it will increased by 2.
    # Here first we check the condition if node is available and it's next_node
    # available then increase marker1 by 1 and marker2 by 2.
    while marker2 != None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        # If marker1 and marker2 equals then cycle exists because if it's cycle
        # then faster marker2 will cross the slower marker1 at some point.
        if marker2 == marker1:
            return True
    # Otherwise no cycle exists.
    return False

# Here checking for my solutions.
a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c

print(check_cycle(a))


d = Node(1)
e = Node(2)
f = Node(3)

d.next_node = e
e.next_node = f
f.next_node = d

print(check_cycle(d))
