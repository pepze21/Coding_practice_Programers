from collections import defaultdict

def solution(clothes):
    kinds = defaultdict(int)
    for cloth in clothes:
        kinds[cloth[1]] += 1
    answer = 1
    for kind in kinds:
        answer *= (kinds[kind] + 1)
    return answer - 1