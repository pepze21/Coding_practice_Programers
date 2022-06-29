def solution(m, n, puddles):
    grid = [[0] * (n + 1) for _ in range(m + 1)]
    for puddle in puddles:
        grid[puddle[0]][puddle[1]] = -1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if ((i == 1) and (j == 1)):
                grid[1][1] = 1
                continue
            if (grid[i][j] == -1):
                grid[i][j] = 0
            else:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[m][n] % 1000000007