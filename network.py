# k : node number
def dfs(n, visited_list, k, computers):
    visited_list[k] = 1
    for i in range(n):
        if (visited_list[i] == 0 and computers[k][i] == 1):
            dfs(n, visited_list, i, computers)    

def solution(n, computers):
    # 0 : not visited, 1: visited
    visited_list = [0 for i in range(n)]
    answer = 0
    
    for i in range(n):
        if (visited_list[i] == 0):
            dfs(n, visited_list, i, computers)
            answer += 1
    return answer