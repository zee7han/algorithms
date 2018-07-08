def mergeSort(arr):
    if (len(arr) < 2):
        return arr

    middle = len(arr)//2
    left = arr[:middle]
    right = arr[middle:]

    leftSort = mergeSort(left)
    rightSort = mergeSort(right)
    return merge(leftSort, rightSort)

def merge(left,right):
    leftIndex = 0
    rightIndex = 0
    result = []

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex]< right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex+=1
        else:
            result.append(right[rightIndex])
            rightIndex+=1

    result += left[leftIndex: ]
    result += right[rightIndex: ]

    return result




l = [2,1,4,3,6,5]
print(mergeSort(l))
