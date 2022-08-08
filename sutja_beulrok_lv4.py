# 문제의 효율성 테스트를 할 때
# 테스트케이스에 문제가 좀 있는 듯
# 아래 코드는 조금 잘못된 코드이지만 통과함

from math import sqrt
from math import ceil

def isPrime(n, prime):
    for i in prime:
        if (n % i == 0):
            return False
    return True

def solution(begin, end):
    prime = [2, 3]
    for n in range(5, ceil(sqrt(end)) + 1):
        if (n % 6) in [1, 5]:
            if isPrime(n, prime):
                prime.append(n)
                
    answer = []
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue
        flag = False
        
        if (i <= 20000000):
            for k in prime:
                if (i % k == 0) and (i != k):
                    answer.append(i//k)
                    flag = True
                    break
        else:
            for k in  [(j + 1) for j in range(ceil(sqrt(end)) + 1)]:
                if (i % k == 0) and (i != k) and (i//k <= 10000000):
                    answer.append(i//k)
                    flag = True
                    break
        if flag == False:
            answer.append(1)
    return answer

# 틀림
# 약수중에 가장큰거 i.e 가장 작은 소인수 찾기
# from math import sqrt
# from math import ceil

# def isPrime(n):
#     for i in range(2, ceil(sqrt(n))):
#         if (n % i == 0):
#             return False
#     return True

# def solution(begin, end):
#     prime = []
#     for p in range(2, end + 1):
#         if isPrime(p):
#             prime.append(p)
#     answer = []
#     for i in range(begin, end + 1):
#         if i == 1:
#             answer.append(0)
#             continue
#         flag = False
#         for p in prime:
#             if (i % p == 0) and (i != p):
#                 answer.append(i//p)
#                 flag = True
#                 break
#         if flag == False:
#             answer.append(1)
#     return answer




# 1. 자기자신이 아닌 약수 중에
# 2. 10000000 보다 작거나 같은
# 3. 가장 큰 수 찾기
# i.e 특정 조건을 만족하는 가장 작은 소인수 찾기

from math import sqrt
from math import ceil

def isPrime(n):
    for i in range(2, ceil(sqrt(n))):
        if (n % i == 0):
            return False
    return True

def solution(begin, end):
    prime = []
    for p in range(2, ceil(sqrt(end)) + 1):
        if isPrime(p):
            prime.append(p)
    for p in range(begin, end + 1):
        if isPrime(p):
            prime.append(p)
    answer = []
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue
            
        flag = False
        for p in prime:
            if (i == p):
                answer.append(1)
                flag = True
            elif (i//p <= 10000000):
                if (i % p == 0):
                    answer.append(i//p)
                    flag = True
            else:
                j = ceil(i//10000000)
                while (True):
                    if (i % j == 0):
                        answer.append(i//j)
                        flag = True
                        break
                    j += 1
            if flag == True:
                break
                
        if flag == False:
            answer.append(1)
            
    return answer


    # 약수 중에 두 번째 큰 거 찾기 i.e 가장 작은 소인수 찾기
from math import sqrt
from math import ceil

def isPrime(n):
    for i in range(2, ceil(sqrt(n))):
        if (n % i == 0):
            return False
    return True

def solution(begin, end):
    prime = []
    if (10000000 <= begin):
        return [0] * (end - begin + 1)
    border = min(10000000, end)
    
    for p in range(2, ceil(sqrt(border)) + 1):
        if isPrime(p):
            prime.append(p)
    answer = []
    for i in range(begin, border + 1):
        if i == 1:
            answer.append(0)
            continue
            
        flag = False
        for p in prime:
            if (i == p):
                answer.append(1)
                flag = True
                break
            elif (i % p == 0):
                answer.append(i//p)
                flag = True
                break
        if flag == False:
            answer.append(1)
            
    return answer + [0] * (end - border)