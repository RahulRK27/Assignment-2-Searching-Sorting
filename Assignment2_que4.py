##Q:4
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    
    return arr
arr = [6, 2, 3, 8, 1, 9, 4, 7, 5]
sorted_arr = insertion_sort(arr)
print(sorted_arr)
