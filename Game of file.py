def gameOfLife(board):
    m, n = len(board), len(board[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    original = [[board[i][j] for j in range(n)] for i in range(m)]

    for i in range(m):
        for j in range(n):
            live_neighbors = 0

            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and original[ni][nj] == 1:
                    live_neighbors += 1

            if original[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = 0  
            elif original[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 1  
    return board


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(gameOfLife(board))
