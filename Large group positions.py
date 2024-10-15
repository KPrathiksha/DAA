def large_group_positions(s):
    i, n = 0, len(s)
    ans = []
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        if j - i >= 3:
            ans.append([i, j - 1])
        i = j
    return ans

# Example usage
s = "abbxxxxzzy"
print(large_group_positions(s))
