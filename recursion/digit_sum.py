def sum_func(n):
    mod = n % 10
    if n == 0:
        return 0
    return mod + sum_func(n//10)

print(sum_func(4321))
print(sum_func(43346))
print(sum_func(987654321))


def sum_func2(n):
    if len(str(n)) == 1:
        return n
    return n%10 + sum_func(n//10)

print(sum_func2(4321))
print(sum_func2(43346))
print(sum_func2(987654321))
