# In  this we used the stack for checking the balanced parantheses
# Also assume that the python list are worked as the stack as we used the
# inbuilt functions of python list to make it behave as a stack
def balance_check(s):
    # Here check for the edge case if the number of total in string is not even
    # then it will be not balanced parantheses
    if len(s)%2 != 0:
        return False
    # Create a set of all three type of opening bracket
    opening = set('([{')
    # Create a set of tuple of all kind of matches that we need to check
    matches = set([('(',')'),('[',']'),('{','}')])
    # Create a empty list that work as a stack for me.
    stack = []
    for paren in s:
        # Check for every parantheses in string if it is in
        # opening set then push into stack
        if paren in opening:
            stack.append(paren)
        # If not in opening set
        else:
            # If Stack is not empty then pop the top elemnent
            if len(stack) != 0:
                last_open = stack.pop()
                # If the tuple of last_open and paren is not in matches
                # then return false
                if (last_open,paren) not in matches:
                    return False
    # Here check if stack empty return true otherwise return false
    return len(stack) == 0





print(balance_check('[[{{(())}}]]'))
print(balance_check('[]{}({[]})'))
print(balance_check('[]({}{[]'))
print(balance_check('[]({}{{{[[[]]}}[]'))
print(balance_check('['))


# This is almost use same assumptions as the first solution a little difference
# in else condition
def balance_check2(s):
    if len(s)%2 != 0:
        return False

    opening = set('([{')
    matches = set([('(',')'),('[',']'),('{','}')])
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            # Here check for stack is empty and return false
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open,paren) not in matches:
                return False
    return len(stack) == 0





print(balance_check2('[[{{(())}}]]'))
print(balance_check2('[]{}({[]})'))
print(balance_check2('[]({}{[]'))
print(balance_check2('[]({}{{{[[[]]}}[]'))
print(balance_check2('['))
