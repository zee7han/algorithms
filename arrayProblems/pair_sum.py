# This function gives output in order of n square
def pair_sum(array, k):
    l = len(array)
    count = 0
    # Here we are just going through the nested loop to add the elements of array and check its presence
    for i in range(l-2):
        for j in range(i+1, l):
            if (array[i] + array[j]) == k:
                count += 1
    return count


print(pair_sum([1,2,3,4,5,6,7,8,9,10,11,12,13],10))
print(pair_sum([1,2,3,4,5,6,7,8,9,10,11,12,13],11))


# This function gives the output in order of n
def pair_sum2(array, k):
    if len(array) < 2:
        return
    # Here we are create the two sets for tracking seen elements and output pair
    seen = set()
    output = set()

    for num in array:
        # Here check the difference of total with the number
        target = k - num

        # if difference number available in seen set then its sum with current
        # number must equal with total number k
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target), max(num,target)))
    return len(output)

print(pair_sum2([1,3,2,2],4))
