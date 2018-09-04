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


def merge_sort2(arr):

    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort2(left_half)
        merge_sort2(right_half)

        i=0
        j=0
        k=0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1

            else:
                arr[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
    

print(merge_sort2(l))
