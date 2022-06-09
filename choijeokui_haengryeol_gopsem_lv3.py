from collections import defaultdict

def solution(matrix_sizes):
    answer = 0
    sizes = []
    for item in matrix_sizes:
        sizes.append(item[0])
    sizes.append(item[1])
    
    dp = defaultdict(lambda: defaultdict(int))
    
    for n in range(2, len(sizes)):
        for i in range(len(sizes) - n):
            k = 1
            dp[i][n] = dp[i][k] + dp[i + k][n - k] + sizes[i] * sizes[i + k] * sizes[i + n]
            k += 1            
            while (k < n):
                dp[i][n] = min(dp[i][n], dp[i][k] + dp[i + k][n - k] + sizes[i] * sizes[i + k] * sizes[i + n])
                k += 1
                
    return dp[0][len(matrix_sizes)]

# 잘못 짬
# def solution(matrix_sizes):
#     answer = 0
#     sizes = []
#     for i, item in enumerate(matrix_sizes):
#         sizes.append((item[0], i))
#     sizes.append((item[1], len(matrix_sizes)))
    
#     indices = sorted(sizes[1:-1], reverse=True)
    
#     for _, i in indices:
#         answer += sizes[i-1][0]*sizes[i][0]*sizes[i+1][0]
#     print(answer)
    
# 시간초과
# cnts = []
# def dfs(sizes, cnt):
#     global cnts
#     if len(sizes) == 2:
#         cnts.append(cnt)
#         return
#     for i in range(1, len(sizes) - 1):
#         dfs(sizes[:i] + sizes[i + 1:], cnt + sizes[i - 1] * sizes[i] * sizes[i + 1])
    
# def solution(matrix_sizes):
#     global cnts
#     sizes = []
#     for item in matrix_sizes:
#         sizes.append(item[0])
#     sizes.append(item[1])
    
#     dfs(sizes, 0)
#     return min(cnts)