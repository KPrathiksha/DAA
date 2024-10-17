def find_min_max(arr):
    min_value = arr[0]
    max_value = arr[0]

    for num in arr[1:]:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return min_value, max_value

# Input
N = 8
a = [5, 7, 3, 4, 9, 12, 6, 2]

# Find Min and Max
min_value, max_value = find_min_max(a)

# Output
print("Min =", min_value, "Max =", max_value)
