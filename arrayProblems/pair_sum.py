# This function gives output in order of n square
def pair_sum(array, k):
    l = len(array)
    count = 0
    for i in range(l-2):
        for j in range(i+1, l):
            if (array[i] + array[j]) == k:
                count += 1
    return count


print(pairSum([1,2,3,4,5,6,7,8,9,10,11,12,13],10 ))
print(pairSum([1,2,3,4,5,6,7,8,9,10,11,12,13],11 ))
