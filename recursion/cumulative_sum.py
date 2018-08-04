# Here we find the cumulative sum for a number n.
def rec_sum(n):
    # Handling the base case
    if n == 0:
        return 0
    # Handling the recusive case and call function for n-1 and add it to n.
    else:
        return n + rec_sum(n-1)

print(rec_sum(5))
print(rec_sum(8))
print(rec_sum(10))
