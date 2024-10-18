def generate_subsets(arr):
    n = len(arr)
    subsets_sums = []
    for i in range(2 ** n):
        subset_sum = 0
        for j in range(n):
            if i & (1 << j):  # If j-th bit is set, include arr[j] in the sum
                subset_sum += arr[j]
        subsets_sums.append(subset_sum)
    return subsets_sums

def meet_in_the_middle(arr, exact_sum):
    n = len(arr)
    left, right = arr[:n // 2], arr[n // 2:]
    left_sums = generate_subsets(left)
    right_sums = generate_subsets(right)
    right_sums_set = set(right_sums)
    for s in left_sums:
        if (exact_sum - s) in right_sums_set:
            return True  
    return False  
arr = [1, 3, 9, 2, 7, 12]
exact_sum = 15
result = meet_in_the_middle(arr, exact_sum)
print(f"Is there a subset with sum {exact_sum}? {'Yes' if result else 'No'}")
