def solution(n):
    if (n % 2 == 1):
        return 0
    
    k = n//2
    
    a = [0] * k
    a[0] = 3
    if (k == 1):
        return a[0]
    a[1] = 11
    if (k == 2):
        return a[1]

    for i in range(2, k):
        a[i] = (3 * a[i - 1]) + (2 * sum(a[:i-1])) + 2

    return a[-1] % 1000000007