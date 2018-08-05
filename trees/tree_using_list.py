def binary_tree(r):
    return [[r],[],[]]

def insert_left_child(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[new_branch,t,[]])
    else:
        root.insert(1,[new_branch,[],[]])
    return root

def insert_right_child(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[new_branch,[],t])
    else:
        root.insert(2,[new_branch,[],[]])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]



r = binary_tree(3)
insert_left_child(r,4)
insert_left_child(r,5)
insert_right_child(r,6)
insert_right_child(r,7)

l = get_left_child(r)
print(l)
set_root_val(l,9)
print(r)
