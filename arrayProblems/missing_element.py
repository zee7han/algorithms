# Here finder find the missing element of arr2
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
