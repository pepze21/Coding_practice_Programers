def solution(d, budget):
    d = sorted(d)
    for i in range(len(d) - 1):
        d[i + 1] += d[i]
    for i in range(len(d)):
        if d[i] > budget:
            return i
    return len(d)