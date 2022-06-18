from math import ceil

def solution(citations):
    u = len(citations)
    l = 0
    
    while (u - l > 0):
        m = (u + l + 1) // 2
        cnt = 0
        for citation in citations:
            if citation >= m:
                cnt += 1
            if cnt == m:
                break
        if cnt == m:
            l = m
        else:
            u = m - 1
    
    return u