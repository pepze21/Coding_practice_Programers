def solution(n):
    grid = [[0] * (i + 1) for i in range(n) ]
    d = [[+1, +0],
         [+0, +1],
         [-1, -1]]
    ptrn = 0
    i = -1
    j = 0
    cnt = 0
    while (cnt < n * (n + 1) // 2):
        # if (out of grid) or (visited) => change pattern
        if (0 <= i + d[ptrn][0] < n) and (0 <= j + d[ptrn][1] <= i + d[ptrn][0]):
            if (grid[i + d[ptrn][0]][j + d[ptrn][1]] != 0):
                ptrn = (ptrn + 1) % 3
        else:
            ptrn = (ptrn + 1) % 3
        i += d[ptrn][0]
        j += d[ptrn][1]
        cnt += 1
        grid[i][j] = cnt
    answer =[]
    for row in grid:
        answer += row
    return answer