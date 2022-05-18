from math import ceil
from math import sqrt

def is_prime(p):
    if p == 1:
        return False
    for i in range(2, ceil(sqrt(p)) + 1):
        if p != i and p % i == 0:
            return False
    return True

def solution(n, k):
    if k < 10:
        s = ''
        while (n > 0):
            n, r = divmod(n, k)
            s = str(r) + s
    else:
        s = str(n)
    
    answer = 0
    for p in s.split('0'):
        if (p != '') and is_prime(int(p)):
            answer += 1
    
    return answer