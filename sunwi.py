# 13분

def dfs(curr_player, visit, n, directed_graph):
    for next_player in directed_graph[curr_player]:
        if (not visit[next_player]):
            visit[next_player] = 1
            dfs(next_player, visit, n, directed_graph)

def solution(n, results):
    win_graph = {i:[] for i in range(1, n + 1)} # directed edge of i-win
    lose_graph = {i:[] for i in range(1, n + 1)} # directed edge of i-lose
    for result in results:
        win_graph[result[0]].append(result[1])
        lose_graph[result[1]].append(result[0])
    answer = 0
    for i in range(1, n + 1):
        visit = [1] + [0 for _ in range(n)] # do not use visit[0]
        visit[i] = 1
        dfs(i, visit, n, win_graph) # winning direction exhaustive search
        dfs(i, visit, n, lose_graph) # losing direction exhaustive search
        if (0 not in visit):
            answer += 1
    return answer