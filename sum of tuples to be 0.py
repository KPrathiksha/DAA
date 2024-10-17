def four_sum_count(A, B, C, D):
    sums = {}
    
    # Store sums of pairs from A and B in a dictionary
    for i in A:
        for j in B:
            sums[i + j] = sums.get(i + j, 0) + 1

    counter = 0
    
    # Check if the negated sum from pairs in C and D exists in the dictionary
    for i in C:
        for j in D:
            counter += sums.get(-(i + j), 0)
    
    return counter

# Example usage
print(four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]))
