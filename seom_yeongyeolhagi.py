# 걍 아무생각없이 그리디로 짰는데 이게 프림(Prim's)알고리즘이라고 함...

def solution(n, costs):
    edge_graph = {i:[] for i in range(n)}
    for cost in costs:
        edge_graph[cost[0]].append(cost[1])
        edge_graph[cost[1]].append(cost[0])
    
    cost_table = [[999999999] * n for _ in range(n)] # 999,999,999 means the edge doesn't exist
    for cost in costs:
        cost_table[cost[0]][cost[1]] = cost[2]
        cost_table[cost[1]][cost[0]] = cost[2]
    
    visit = [0] * n
    visit[0] = 1 # starting node : 0
    
    answer = 0
    while (0 in visit):
        min_cost = 999999999
        next_node = -1 # initialize
        
        for i in [_ for _ in range(len(visit)) if visit[_] == 1]:
            for j in [_ for _ in range(len(visit)) if visit[_] == 0]:
                if (cost_table[i][j] < min_cost):
                    min_cost = cost_table[i][j]
                    next_node = j # finding the minimum cost node by Greedy
        answer += min_cost
        visit[next_node] = 1
    return answer