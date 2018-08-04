# here we implement the permutation function to get all possible permutation
# of string.
def permute(s):
    # Initialize a empty list for storung the result.
    out = []
    # Handling the base case and add the string of len 1 to list.
    if len(s) == 1:
        out = [s]
    else:
        # Loop through the letter of string and enumerate gives the index and
        # letter in for in loop.
        for i,let in enumerate(s):
            # recursively call the permute and loop through each perm to
            # get one permutation.
            for perm in permute(s[:i]+s[i+1:]):
                out += [let + perm]
    return out

print(permute('abc'))
