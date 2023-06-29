def bubblesort(arr):
    n = len(arr)
    for k in range(0,n):
        for i in range (0,n-k-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

arr = [12, 6, 8, 9, 5, 1, 7]
print("Before Sorting : {}".format(arr))
bubblesort(arr)
print("After Sorting: {}".format(arr))