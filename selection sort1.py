# Selection sort implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Find the index of the minimum element in the remaining array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Input and sorting
arr = [5, 2, 9, 1, 5, 6]
selection_sort(arr)
print("Sorted array:", arr)
