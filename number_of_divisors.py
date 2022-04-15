# restrictions
# 1 ≤ left ≤ right ≤ 1000

from math import sqrt
from math import ceil

# we need only these prime numbers because of restrictions
PRIME_NUMBERS = [2, 3, 5, 7, 11 ,13, 17, 19, 23, 29, 31, 37]

def number_of_divisors(k):
    upper_bound = ceil(sqrt(k))
    i = 0
    cnt = 0
    factors = []
    while(upper_bound >= PRIME_NUMBERS[i]):
        if (k % PRIME_NUMBERS[i] == 0):
            k //= PRIME_NUMBERS[i]
            cnt += 1
        else:
            if (cnt > 0):
                factors.append(cnt)
            cnt = 0
            i += 1
    if (k != 1):
        factors.append(1)
        
    result = 1
    for factor in factors:
        result *= (factor + 1)
        
    return result

def solution(left, right):
    answer = 0
    for k in range(left, right + 1):
        nod = number_of_divisors(k)
        if (nod % 2 == 0):
            answer += k
        else:
            answer -= k
        
    return answer