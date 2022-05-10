def solution(n, works):
    works.sort(reverse=True)
    s = max(sum(works) - n, 0)
    if s == 0:
        return 0
    u = max(works)
    l = 0
    while (u - l >= 0):
        t = 0
        m = (u + l + 1) // 2
        for work in works:
            t += min(work, m)
        if (u - l == 0):
            break
        if t <= s:
            l = m
        else:
            u = m - 1
    for i in range(len(works)):
        works[i] = min(works[i], u)
    for i in range(s - t):
        works[i] += 1
    return sum(map(lambda x: x**2, works))