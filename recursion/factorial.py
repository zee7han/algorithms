# Here we find the factorial for a number n.
def fact(n):
    # Handling the base case.
    if n == 0 or n == 1:
        return 1
    # Handling the recursion and call fact recusively for n-1.
    else:
        return n * fact(n-1)

print(fact(5))
print(fact(6))
print(fact(10))
