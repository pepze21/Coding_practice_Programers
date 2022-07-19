from collections import deque

def metric(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

def solution(begin, target, words):
    edge = {word:[] for word in words}
    edge[begin] = []
    edge[target] = []
    for word1 in edge.keys():
        for word2 in edge.keys():
            if metric(word1, word2) == 1:
                edge[word1].append(word2)
    if (target not in words) or (edge[target] == []):
        return 0
    visit = {key:0 for key in edge.keys()}
    distance = 1
    
    # bfs
    q = deque([begin])
    while q:
        for i in range(len(q)):
            v = q.popleft()
            for word in edge[v]:
                if target in edge[v]:
                    return distance
                elif visit[word] == 0:
                    visit[word] = 1
                    q.append(word)
        distance += 1
    return 0