def partition (array, lb, ub):
    pivot = array[lb]            # Pivot elemenet can be any element in array
    start = lb + 1               # lb - lower bound
    end = ub                     # ub - upper bound
    
    while True:
        while array[start] <= pivot and start <= end:
            start += 1
        while array[end] > pivot and start <= end:
            end -= 1
        
        if start < end:
            array[start], array[end] = array[end], array[start]
        else:
            break

    array[lb], array[end] = array[end], array[lb]
    return end

def quick_sort (array, start, end):
    if start >= end:
        return
    
    k = partition(array, start, end)
    quick_sort(array, start, k-1)    
    quick_sort(array, k+1, end)    
    
data = [12, 7, 8, 9, 67, 89, 100, 34]
print("Before Sorting : {}".format(data))

lb = 0
ub = len(data)-1
quick_sort(data, lb, ub)
print("After Sorting: {}".format(data))