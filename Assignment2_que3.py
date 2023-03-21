## Q:3
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = []
    right = []
    equal = []
    
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    
    return quick_sort(left) + equal + quick_sort(right)
arr = [6, 2, 3, 8, 1, 9, 4, 7, 5]
sorted_arr = quick_sort(arr)
print(sorted_arr)
