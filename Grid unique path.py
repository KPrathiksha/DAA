def uniquePaths(m: int, n: int) -> int:
    f = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            f[i][j] = f[i - 1][j] + f[i][j - 1]
    return f[m - 1][n - 1]

m = 3
n = 7
print(uniquePaths(m, n))  # Output: 28
