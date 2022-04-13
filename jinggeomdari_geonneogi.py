def solution(stones, k):
    high = max(stones)
    low = 1
    len_stones = len(stones)
    distance = 1
    
    while (True):
        middle = (high + low + 1) // 2
        distance = 1
        for i in range(len_stones):
            if (stones[i] < middle):
                distance += 1
                if (distance > k):
                    high = middle - 1
                    break
            else:
                distance = 1
        if (distance <= k):
            low = middle
        if (high == low):
            return high