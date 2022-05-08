def solution(s):
    return len(s.lower().replace('p', '')) == len(s.lower().replace('y', ''))