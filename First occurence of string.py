def strStr(haystack, needle):
    n, m = len(haystack), len(needle)

    for i in range(n - m + 1):
        if haystack[i : i + m] == needle:
            return i  
    return -1

haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))  
