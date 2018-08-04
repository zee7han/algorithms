# Here we implement a function to add all digit of a number.
def sum_func(n):
    # Get the last digit of a number by taking modulus.
    mod = n % 10
    # handling the base case.
    if n == 0:
        return 0
    # Handling the recusrion case and call function for remaining digit by
    # dividing it by 10.
    return mod + sum_func(n//10)

print(sum_func(4321))
print(sum_func(43346))
print(sum_func(987654321))

# Here is the second approach for the same.
def sum_func2(n):
    # handling the base case.
    if len(str(n)) == 1:
        return n
    # Handling the recusrion case and call function for remaining digit by
    # dividing it by 10.
    return n%10 + sum_func(n//10)

print(sum_func2(4321))
print(sum_func2(43346))
print(sum_func2(987654321))
