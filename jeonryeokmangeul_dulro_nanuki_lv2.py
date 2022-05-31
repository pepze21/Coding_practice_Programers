from collections import defaultdict
from copy import deepcopy

def dfs(curr_node, n, edges, visit):
    for next_node in edges[curr_node]:
        if not visit[next_node]:
            visit[next_node] = 1
            dfs(next_node, n, edges, visit)
            
def solution(n, wires):
    edges = defaultdict(list)
    diffs = []
    
    for i in range(len(wires)):
        wires_copy = deepcopy(wires)
        del wires_copy[i]
        edges = defaultdict(list)
        for wire in wires_copy:
            edges[wire[0]].append(wire[1])
            edges[wire[1]].append(wire[0])
            
        visit = [0] * (n + 1)
        visit[1] = 1
        dfs(1, n, edges, visit)
        diffs.append(abs(2 * sum(visit) - n))
        
    return min(diffs)