# implementation of reversing the stirng using recursion.
def reverse(s):
    # handling the base case.
    if len(s) == 1:
        return s
    # handling the recursioncase.
    else:
        return reverse(s[1:]) + s[0]


print(reverse('hello'))
