from math import sqrt
from math import ceil

num_set = set()

def isPrime(k):
    if k == 0 or k == 1:
        return False
    else:
        for i in range(2, k):
            if k % i == 0:
                return False
    return True

def dfs(string, pos_num):
    global num_set
    if string == '':
        return
    for i, s in enumerate(string):
        pos_num += s
        if isPrime(int(pos_num)):
            num_set.add(str(int(pos_num)))
        dfs(string.replace(s, '', 1), pos_num)
        pos_num = pos_num[:-1]

def solution(numbers):
    global num_set
    dfs(numbers, '')
    return len(num_set)