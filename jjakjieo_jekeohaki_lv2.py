def solution(s):
    t = []
    for i in range(len(s)):
        if (not t) or (s[i] != t[-1]):
            t.append(s[i])
        else:
            t.pop()
    return 0 if t else 1