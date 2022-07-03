import sys
sys.setrecursionlimit(10**6)

answer = []

def dfs(i, j, k, cnt, visit, grid, d):
    global answer
    if visit[i][j][k] == 1:
            answer.append(cnt)
    else:
        visit[i][j][k] = 1
        di, dj = d[k]
        i = (i + di) % len(grid)
        j = (j + dj) % len(grid[0])
        if grid[i][j] == 'L':
            k = (k + 1) % 4
        elif grid[i][j] == 'R':
            k = (k - 1) % 4
        cnt += 1
        dfs(i, j, k, cnt, visit, grid, d)

def solution(grid):
    global answer
    d = [[+1, 0], # direction
         [0, +1], #   2
         [-1, 0], # 3   1
         [0, -1]] #   0
    visit = [[[0] * 4 for j in range(len(grid[0]))] for i in range(len(grid))]

    for i  in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                if visit[i][j][k] == 0:
                    dfs(i, j, k, 0, visit, grid, d)

    return sorted(answer)