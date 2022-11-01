import collections
# Here finder find the missing element of arr1 in arr2
def finder(arr1, arr2):
    # sort the both lists
    arr1.sort()
    arr2.sort()
    # Here we loop throigh the arr1 from 0 to length-1
    for i in range(0,len(arr1)-1):
        # Check this condition till the lenght of arr2 or if arr2 is not out of bounds
        if i < len(arr1)-2:
            if arr1[i] != arr2[i]:
                print(f"{arr1[i]} is the missing element")
                return
        # Here we are handling the missing element is the last element of the arr1
        # This will simply print the last element of arr1.
        else:
            print(f"{arr1[i+1]} is the missing element")
            return

finder([1,4,2,53,54,2,4],[2,4,53,1,54,4])
finder([1,2,3,4,5,6],[2,4,3,1,5])



# This approach will find the element in O(NlogN)
def finder2(arr1, arr2):
    # Here we sort the both lists
    arr1.sort()
    arr2.sort()
    # Here we loop through the zip of both element
    # zip return the tuple of element of same index from both lists
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            print(f"{num1} is the missing element")
            return num1
    # Here we return the last element of the arr1
    print(f"{arr1[-1]} is the missing element")
    return arr1[-1]

finder2([1,4,2,53,54,2,4],[2,4,53,1,54,4])
finder2([1,2,3,4,5,6],[2,4,3,1,5])



# This approach will take around the O(N) time complexity
def finder3(arr1, arr2):
    # this create the dictionary which not throw error while a key is not found
    dic = collections.defaultdict(int)
    # Update the dic if key available update it by 1 or not available then create new key and update it it
    for num in arr2:
        dic[num] += 1
    # check if arr1 key present in dic then return number otherwise decrease the count of that number
    for num in arr1:
        # Return the number that is missing
        if dic[num] == 0:
            print(f"{num} is the missing element")
            return num
        # decrease the count of that number
        else:
            dic[num] -= 1


finder3([1,4,2,53,54,2,4],[2,4,53,1,54,4])
finder3([1,2,3,4,5,6],[2,4,3,1,5])


# Here i am using the clever trick that using the XOR operator
def finder4(arr1, arr2):
    result =0
    # Loop through the list after concatenation
    for num in arr1+arr2:
        # XOR the every result with the number
        result^=num
    return result

print(finder4([1,4,2,53,54,2,4],[2,4,53,1,54,4]))
print(finder4([1,2,3,4,5,6],[2,4,3,1,5]))
