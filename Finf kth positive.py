def findKthPositive(arr, k):
    if arr[0] > k:
        return k
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] - mid - 1 >= k:
            right = mid
        else:
            left = mid + 1

    return arr[left - 1] + k - (arr[left - 1] - (left - 1) - 1)

arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositive(arr, k))  
