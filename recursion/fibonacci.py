# Here implementation of Nth fibonacci number using iteration.
def fib_iter(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

print(fib_iter(10))
print(fib_iter(23))

# Here implementation of Nth fibonacci number using recursion.
def fib_rec(n):
    # Handling the base case.
    if n == 0 or n == 1:
        return n
    # Handling the recursion case calling fib_rec for n-1 and n-2.
    else:
        return fib_rec(n-1) + fib_rec(n-2)


print(fib_rec(10))
print(fib_rec(23))

# Here implementation of Nth fibonacci number using dynamic programming.
# We have to initialize the cache the of size larger than the n.
cache = [None] * (25)
def fib_dyn(n):
    # Handling the base case.
    if n == 0 or n == 1:
        return n
    # checking for the cache and lookup table.
    elif cache[n] != None:
        return cache[n]
    # Handling the recursion case calling fib_rec for n-1 and n-2 and store
    # result into cache and return it from cache.
    else:
        cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
        return cache[n]


print(fib_dyn(10))
print(fib_dyn(23))
