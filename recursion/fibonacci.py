def fib_iter(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

print(fib_iter(10))
print(fib_iter(23))

def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)


print(fib_rec(10))
print(fib_rec(23))

cache = [None] * (25)
def fib_dyn(n):
    if n == 0 or n == 1:
        return n
    elif cache[n] != None:
        return cache[n]
    else:
        cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
        return cache[n]


print(fib_dyn(10))
print(fib_dyn(23))
