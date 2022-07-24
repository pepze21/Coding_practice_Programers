from math import ceil
from math import sqrt

def solution(n, k):
    k -= 1
    remain = [(i + 1) for i in range(n)]
    answer = []
    a = 1
    for i in range(1, n):
        a *= i
    while (i > 0):
        q = k // a
        answer.append(remain[q])
        del remain[q]
        k = k % a
        a //= i
        i -= 1
    return answer + remain