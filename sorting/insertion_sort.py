def insertion_sort(arr):
    for i in range(1,len(arr)):
        position = i
        current_value = arr[i]
        print("position and current_value before", position, current_value)

        while position > 0 and arr[position-1] > current_value:
            arr[position] = arr[position-1]
            position = position-1

        print("position and current_value after change -----------", position)

        arr[position] = current_value



arr = [1,4,2,3,7,86,9]
insertion_sort(arr)
print(arr)
