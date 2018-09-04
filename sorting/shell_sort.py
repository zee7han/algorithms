def shell_sort(arr):
    sublist_count = len(arr)//2

    while sublist_count > 0:
        for start in range(sublist_count):
            print("Value of start is-------------------------------------------------------", start, sublist_count)
            gap_insertion_sort(arr,start,sublist_count)
        print("Value of sublist_count is-------------------", sublist_count)

        sublist_count = sublist_count//2

def gap_insertion_sort(arr,start,gap):

    for i in range(start+gap,len(arr),gap):
        print("Value of i is-----",i)
        current_value = arr[i]
        position = i

        while position >= gap  and arr[position-gap] > current_value:
            arr[position] = arr[position-gap]
            position = position-gap

        arr[position] = current_value



arr = [1,4,2,3,7,86,9]
shell_sort(arr)
print(arr)
