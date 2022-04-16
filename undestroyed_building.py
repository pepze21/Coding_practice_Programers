# 누적합 이용 45분

def solution(board, skill):
    prefix_sum = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    SIGN = [0, -1 , 1]
    for s in skill:
        sign = SIGN[s[0]]
        prefix_sum[s[1]][s[2]] += sign * s[-1]
        prefix_sum[s[1]][s[4] + 1] += -sign * s[-1]
        prefix_sum[s[3] + 1][s[2]] += -sign * s[-1]
        prefix_sum[s[3] + 1][s[4] + 1] += sign * s[-1]
        
    for i in range(len(prefix_sum)):
        for j in range(len(prefix_sum[0]) - 1):
            prefix_sum[i][j + 1] += prefix_sum[i][j]
    for j in range(len(prefix_sum[0])):
        for i in range(len(prefix_sum) - 1):
            prefix_sum[i + 1][j] += prefix_sum[i][j]
            
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += prefix_sum[i][j]
            if (board[i][j] > 0):
                answer += 1
    return answer


# 13분. 이코드는 정확성은 통과했으나, 효율성은 전부 시간초과
# SIGN = [0, -1, 1]
# def solution(board, skill):
#     for one_skill in skill:
#         effect = SIGN[one_skill[0]] * one_skill[-1]
#         for i in range(one_skill[1], one_skill[3] + 1):
#             for j in range(one_skill[2], one_skill[4] + 1):
#                 board[i][j] += effect
#     answer = 0
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if (board[i][j] > 0):
#                 answer += 1
#     return answer
