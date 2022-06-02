# 직접구현
def solution(n):
    answer = 0
    while (n > 0):
        n, r = divmod(n, 2)
        answer += r
    return answer

# .count()
# def solution(n):
#     return bin(n).count('1')

# 시간초과
# def solution(n):
#     return sum(map(int, bin(n)[2:]))