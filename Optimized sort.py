def optimized_sort(lst):
    return sorted(lst)

test_input = [64, 25, 12, 22, 11]
expected_output = [11, 12, 22, 25, 64]


result = optimized_sort(test_input)
print("Input: ", test_input)
print("Expected Output: ", expected_output)
print("Actual Output: ", result)

if result == expected_output:
    print("Test passed!")
else:
    print("Test failed.")
