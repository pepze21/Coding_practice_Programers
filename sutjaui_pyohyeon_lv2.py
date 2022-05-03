from math import sqrt
from math import ceil

def solution(n):
    answer = 0
    for k in range(1, ceil(sqrt(n * 2))):
        if ((n - (k * (k + 1)//2)) % k == 0):
            answer += 1
    return answer