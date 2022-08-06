def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    length = len(food_times)
    l = k // length # lower bound
    u = max(food_times) # upper bound
    
    while (u - l > 1):
        m = (l + u) // 2
        s = 0
        for i in range(length):
            if food_times[i] < m:
                s += food_times[i]
            else:
                s += m
        if s <= k:
            l = m
        else:
            u = m
    
    s = 0
    for i in range(length):
        if food_times[i] < l:
            s += food_times[i]
        else:
            s += l
    
    cnt = 0
    for i, time in enumerate(food_times):
        if time > l:
            if cnt == k - s:
                return i + 1
            cnt += 1