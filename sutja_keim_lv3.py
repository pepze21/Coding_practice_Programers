import heapq

def solution(A, B):
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)
    a = heapq.heappop(A)
    while B:
        b = heapq.heappop(B)
        if (a < b):
            answer += 1
            if A:
                a = heapq.heappop(A)
            
    return answer