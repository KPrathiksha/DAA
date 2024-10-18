from itertools import chain, combinations

def all_subsets(arr):
    return chain.from_iterable(combinations(arr, r) for r in range(len(arr) + 1))

def meet_in_the_middle(arr, target):
    n = len(arr)
    left, right = arr[:n // 2], arr[n // 2:]
    left_sums = {sum(subset) for subset in all_subsets(left)}
    right_sums = {sum(subset) for subset in all_subsets(right)}

    closest_sum = float('-inf')
    right_sums = sorted(right_sums)
    for s in left_sums:
        remaining = target - s
        lo, hi = 0, len(right_sums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if right_sums[mid] <= remaining:
                lo = mid + 1
            else:
                hi = mid - 1
        if hi >= 0:
            closest_sum = max(closest_sum, s + right_sums[hi])

    return closest_sum

arr = [45, 34, 4, 12, 5, 2]
target = 42
result = meet_in_the_middle(arr, target)
print(f"The closest sum to the target is: {result}")
