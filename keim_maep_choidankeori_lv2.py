from collections import deque

def solution(maps):
    if (len(maps) == 1) and (len(maps[0]) == 1):
        return 1
    q = deque()
    q.append((0, 0))
    d = [[+1, 0],
         [-1, 0],
         [0, +1],
         [0, -1]]
    
    while (q):
        i, j = q.popleft()
        for di, dj in d:
            if (0 <= i + di) and (i + di < len(maps)) and (0 <= j + dj) and (j + dj < len(maps[0])):
                if maps[i + di][j + dj] == 1:
                    maps[i + di][j + dj] = maps[i][j] + 1
                    q.append((i + di, j + dj))
                    
    if maps[-1][-1] != 1:
        return maps[-1][-1]
    else:
        return -1