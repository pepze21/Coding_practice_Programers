from math import sqrt
from math import ceil

def solution(n):
    # print(ceil(sqrt(n)))
    numbers = [True  for _ in range(n + 1)]
    numbers[0] = False # 0은 소수인가? False
    numbers[1] = False # 1은 소수인가? False
    
    for i in range(ceil(sqrt(n))):
        if (numbers[i] == True):
            for j in range(2, (n // i)  + 1):
                numbers[j*i] = False

    return sum(numbers)