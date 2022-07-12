def solution(s):
    s2 = list(map(int, s.split()))
    return ' '.join(map(str, [min(s2), max(s2)]))