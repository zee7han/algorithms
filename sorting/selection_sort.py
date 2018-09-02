def selection_sort(arr):
    for fills_slot in range(len(arr)-1,0,-1):
        print("Value of fills_slot--------------------------", fills_slot)
        max_position = 0
        for location in range(1,fills_slot+1):
            print("Value of location", location)
            if arr[location] > arr[max_position]:
                max_position = location

        temp = arr[fills_slot]
        arr[fills_slot] = arr[max_position]
        arr[max_position] = temp


arr = [1,4,2,3,7,86,9]
selection_sort(arr)
print(arr)
