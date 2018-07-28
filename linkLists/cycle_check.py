class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None



def check_cycle(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True
    return False


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
