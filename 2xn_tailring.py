def solution(n):
    
    a1 = 1
    a2 = 2
    if n < 3:
        return n
    for _ in range(3, n + 1): 
        answer = a1 + a2
        a1 = a2
        a2 = answer
    return answer % 1000000007