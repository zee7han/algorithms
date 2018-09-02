def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        print("value of n-------------------",n)
        for k in range(n):
            print("value of k",k)
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp


arr =[2,1,4,5,3]
bubble_sort(arr)
print(arr)
