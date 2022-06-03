def solution(board):
    grid = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for i in range(len(board)):
        grid[i + 1][1:] = board[i]

    # prefix_sum
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0]) - 1):
            grid[i][j + 1] += grid[i][j]
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0])):
            grid[i + 1][j] += grid[i][j]
            
    l = min(len(board), len(board[0]))
    while (l > 0):
        for i in range(len(grid) - l):
            for j in range(len(grid[0]) - l):
                if grid[i + l][j + l] - grid[i + l][j] - grid[i][j + l] + grid[i][j] == l**2:
                    return l**2
        l -= 1
    return 0
    
# 정확하지도 않고 느림
# def solution(board):
#     l = min(len(board), len(board[0]))
#     while (l > 0):
#         for i in range(len(board) + 1 - l):
#             for j in range(len(board[0]) + 1 - l):
#                 if l**2 == sum(map(sum, board[i:i + l][j:j + l])):
#                     print(i, j, l)
#                     return l**2
#         l -= 1
#     return 0

# 0111
# 1111
# 1111
# 0010

# 0123
# 1234
# 1234
# 0011

# 0 1 2  3
# 1 3 5  7
# 2 5 8 11
# 2 5 9 12
