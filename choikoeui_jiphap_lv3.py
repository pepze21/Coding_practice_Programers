def solution(n, s):
    if n > s:
        return [-1]
    q, r = divmod(s, n)
    answer = [q] * n
    for i in range(r):
        answer[-1 -i] += 1
    return answer