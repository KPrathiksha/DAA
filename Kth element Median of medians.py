def partition(arr, pivot):
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return left, middle, right

def median_of_medians(arr):
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2] 
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    return median_of_medians(medians)

def kth_smallest(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = median_of_medians(arr)  # Get a good pivot
    left, middle, right = partition(arr, pivot)
    if k <= len(left):
        return kth_smallest(left, k)
    elif k <= len(left) + len(middle):
        return pivot  
    else:
        return kth_smallest(right, k - len(left) - len(middle))

arr = [12, 3, 5, 7, 19]
k = 2
result = kth_smallest(arr, k)
print(f"The {k}-th smallest element is {result}")
