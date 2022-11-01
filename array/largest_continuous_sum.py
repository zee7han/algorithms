# Here we calculate the largest sum in O(N)
def large_cont_sum(arr):
    # If length of list is zero return zero
    if len(arr) == 0:
        return 0
    # Initialize the current sum and max_sum to first element of list
    max_sum = current_sum = arr[0]
    # Loop through the element of the list from second to last bcoz we consider the first element already
    for num in arr[1:]:
        # Check for the max between current_sum and num
        current_sum = max(current_sum+num,num)
        # Get the max_sum from current_sum and max_sum
        max_sum = max(current_sum, max_sum)
    return max_sum

print(large_cont_sum([1,2,3,-3,2,-1]))
print(large_cont_sum([-11,20,31,-31,21,11]))
