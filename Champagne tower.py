def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    f = [[0] * 101 for _ in range(101)]
    f[0][0] = poured  
    for i in range(query_row + 1):
        for j in range(i + 1):
            if f[i][j] > 1:
                excess = (f[i][j] - 1) / 2  
                f[i][j] = 1  
                f[i + 1][j] += excess 
                f[i + 1][j + 1] += excess  
    return min(1, f[query_row][query_glass])

poured = 25
query_row = 6
query_glass = 1
print(champagneTower(poured, query_row, query_glass))  
