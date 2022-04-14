history = [0] # root(sheep)
sheep_minus_wolf = 1
max_sheep = 1

def dfs(info, edges, visited_edges):
    global sheep_minus_wolf, max_sheep
    sum_sheep = 0
    for node in history:
        if (info[node] == 1):
            sum_sheep += 1
    # if (max_sheep != max(max_sheep, sum_sheep)):
    #     print(max_sheep, history, sheep_minus_wolf)
    max_sheep = max(max_sheep, sum_sheep)
    
    for node in history:
        for i in range(len(edges)):
            if (edges[i][0] == node and visited_edges[i] == 0):
                sheep_minus_wolf += info[edges[i][1]] # 다음 노드의 smw를 미리계산
                if (sheep_minus_wolf > 0):
                    history.append(edges[i][1])
                    visited_edges[i] = 1
                    dfs(info, edges, visited_edges)
                    history.pop()
                    visited_edges[i] = 0
                    sheep_minus_wolf -= info[edges[i][1]]
                else:
                    sheep_minus_wolf -= info[edges[i][1]]
                
def solution(info, edges):
    for i in range(len(info)):
        if (info[i] == 1):
            info[i] = -1
        elif (info[i] == 0):
            info[i] = 1
            
    visited_edges = [0 for _ in range(len(edges))]
    dfs(info, edges, visited_edges)
    
    return max_sheep
