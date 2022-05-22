from copy import deepcopy
from collections import deque

def solution(board):
    N = len(board)
    q = deque()
    q.append((0, 0)) # (i, j)

    d = [[+1, 0], # direction
         [-1, 0], #     1
         [0, +1], #   3   2
         [0, -1]] #     0
    
    inf = 999999
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] *= inf
    dp = [deepcopy(board) for _ in range(4)]
    
    while (q):
        i, j = q.popleft()
        for k in range(4): # the direction to go
            di, dj = d[k]
            tmp = []
            for l in range(4): # the direction came from
                if (i == j == 0):
                    tmp.append(dp[l][i][j] + 100)
                elif (k == l):
                    if (dp[l][i][j] != 0):
                        tmp.append(dp[l][i][j] + 100)
                else:
                    if (dp[l][i][j] != 0):
                        tmp.append(dp[l][i][j] + 600)
            if (0 <= i + di < N) and (0 <= j + dj < N) and (dp[k][i + di][j + dj] < inf):
                if (dp[k][i + di][j + dj] == 0):
                    dp[k][i + di][j + dj] = min(tmp)
                    q.append((i + di, j + dj))

                elif (dp[k][i + di][j + dj] > min(tmp)):
                    dp[k][i + di][j + dj] = min(tmp)
                    q.append((i + di, j + dj))

    answer = inf
    for k in range(4):
        if dp[k][-1][-1] != 0 and answer > dp[k][-1][-1]:
            answer = dp[k][-1][-1]
    return answer

# # 11 12 17 18 19 시간초과
# from collections import deque

# def solution(board):
#     q = deque()
#     q.append((0, 0, 0, 0)) # (i, j, cost, direction)
#     d = [[+1, 0],
#          [-1, 0],
#          [0, +1],
#          [0, -1]]
#     inf = 999999
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             board[i][j] *= inf
    
#     while (q):
#         i, j, cost, drct = q.popleft()
#         if board[i][j] == 0:
#             board[i][j] = cost
#         else:
#             board[i][j] = min(board[i][j], cost)
        
#         if (i == (len(board)) - 1) and (j == (len(board[0]) - 1)):
#             continue
#         for k in range(4):
#             di, dj = d[k]
#             if (0 <= i + di < len(board)) and (0 <= j + dj < len(board[0])):
#                 if (drct == k) or (i == j == 0):
#                     next_cost = cost + 100
#                 else:
#                     next_cost = cost + 600
#                 if (board[i + di][j + dj] < inf) and ((board[i + di][j + dj] == 0) or (board[i + di][j + dj] + 500 >= next_cost)):
#                     q.append((i + di, j + dj, next_cost, k))

#     return board[-1][-1]

# from collections import deque

# def solution(board):
#     q = deque()
#     q.append((0, 0, 0, 0))
#     d = [[+1, 0],
#          [-1, 0],
#          [0, +1],
#          [0, -1]]
#     inf = 999999
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             board[i][j] *= inf
#     while (q):
#         i, j, drct, tmp = q.popleft()
#         for k in range(len(d)):
#             di, dj = d[k]
#             if (0 <= i + di) and (i + di < len(board)) and (0 <= j + dj) and (j + dj < len(board[0])):
#                 if (drct == k) or (i + j == 0):
#                     tmp = board[i][j] + 100
#                 else:
#                     tmp = board[i][j] + 600
#                 if (board[i + di][j + dj] < inf):
#                     if (board[i + di][j + dj] == 0):
#                         board[i + di][j + dj] = tmp
#                         q.append((i + di, j + dj, k, tmp))                           
#                     elif (board[i + di][j + dj] >= tmp):
#                         board[i + di][j + dj] = tmp
#                         q.append((i + di, j + dj, tmp))
#     for row in board:
#         print(row)
    
#     return board[-1][-1]